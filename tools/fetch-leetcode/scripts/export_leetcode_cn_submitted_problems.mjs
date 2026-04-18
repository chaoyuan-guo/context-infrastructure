#!/usr/bin/env node

import { writeFile, readFile, mkdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { join, dirname } from "node:path";
import process from "node:process";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const CACHE_DIR = join(SCRIPT_DIR, "../cache");
const DEFAULT_OUTPUT = "./leetcode-cn-submitted-problems.md";
const CACHE_FILE = join(CACHE_DIR, "leetcode-fetch-cache.json");
const LEETCODE_GRAPHQL_URL = "https://leetcode.cn/graphql/";
const LEETCODE_API_URL = "https://leetcode.cn/api/problems/all/";
const PAGE_SIZE = 100;

// 限流策略参数
// 力扣中文站有严格的请求频率限制，通过以下参数控制以避免触发 429/403:
// - REQUEST_DELAY_MS: 普通请求间隔，经测试 300ms 可在速度与稳定性间平衡
// - CODE_FETCH_DELAY_MS: 代码获取间隔更长(1000ms)，因该接口限流更严格
// - CONCURRENCY: 并发数限制为 3，过高会导致大量请求被拒绝
// - MAX_RETRIES & INITIAL_BACKOFF_MS: 失败重试采用指数退避策略
const REQUEST_DELAY_MS = 300;
const CODE_FETCH_DELAY_MS = 1000;
const MAX_RETRIES = 4;
const INITIAL_BACKOFF_MS = 600;
const CONCURRENCY = 3;

function parseArgs(argv) {
  const args = { output: DEFAULT_OUTPUT, skipCode: false, resume: false, verify: false, incremental: false };

  for (let index = 0; index < argv.length; index += 1) {
    const current = argv[index];
    if (current === "--output" || current === "-o") {
      const value = argv[index + 1];
      if (!value) {
        throw new Error("Missing value for --output");
      }
      args.output = value;
      index += 1;
      continue;
    }
    if (current === "--skip-code" || current === "-s") {
      args.skipCode = true;
      continue;
    }
    if (current === "--resume" || current === "-r") {
      args.resume = true;
      continue;
    }
    if (current === "--verify" || current === "-v") {
      args.verify = true;
      continue;
    }
    if (current === "--incremental" || current === "-i") {
      args.incremental = true;
      continue;
    }
    throw new Error(`Unknown argument: ${current}`);
  }

  const enabledModes = [args.resume, args.verify, args.incremental].filter(Boolean).length;
  if (enabledModes > 1) {
    throw new Error("--resume, --verify, and --incremental cannot be used together");
  }

  return args;
}

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

function toNumber(value) {
  if (typeof value === "number" && Number.isFinite(value)) {
    return value;
  }
  if (typeof value === "string" && /^\d+$/.test(value.trim())) {
    return Number(value.trim());
  }
  return null;
}

function formatDateTime(timestamp) {
  if (!timestamp) return "N/A";
  const date = new Date(timestamp * 1000);
  return date.toLocaleString("zh-CN", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }) + " CST";
}

function parseExportedDateTime(value) {
  if (!value || value === "N/A") return null;

  const match = value.trim().match(/^(\d{4})[/-](\d{2})[/-](\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s+CST$/);
  if (!match) {
    throw new Error(`Unsupported date format: ${value}`);
  }

  const [, year, month, day, hour, minute, second] = match;
  return Math.floor(Date.UTC(
    Number(year),
    Number(month) - 1,
    Number(day),
    Number(hour) - 8,
    Number(minute),
    Number(second)
  ) / 1000);
}

async function callWithRetry(fn, label) {
  let attempt = 0;
  let backoff = INITIAL_BACKOFF_MS;

  while (attempt < MAX_RETRIES) {
    try {
      return await fn();
    } catch (error) {
      attempt += 1;
      if (attempt >= MAX_RETRIES) {
        throw new Error(`${label} failed after ${MAX_RETRIES} attempts: ${error.message}`);
      }
      console.log(`  ${label} failed (attempt ${attempt}), retrying in ${backoff}ms...`);
      await sleep(backoff);
      backoff *= 2;
    }
  }

  throw new Error(`${label} failed unexpectedly`);
}

async function callLeetCodeGraphql(session, query, variables) {
  const response = await fetch(LEETCODE_GRAPHQL_URL, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      cookie: `LEETCODE_SESSION=${session}`,
    },
    body: JSON.stringify({ query, variables }),
  });

  if (!response.ok) {
    throw new Error(`GraphQL request failed with status ${response.status}`);
  }

  const payload = await response.json();
  if (Array.isArray(payload.errors) && payload.errors.length > 0) {
    throw new Error(payload.errors.map((item) => item.message).join("; "));
  }

  return payload.data;
}

async function fetchServerSubmitCounts(session) {
  // 用 userProfileQuestions API 获取服务端每题的真实提交次数
  // 用于 --verify 模式：与缓存对比，找出需要重新抓取的题目
  const all = [];
  let skip = 0;
  const first = 100;
  const query = `
    query q($status: StatusFilterEnum!, $skip: Int!, $first: Int!, $sortField: SortFieldEnum!, $sortOrder: SortingOrderEnum!) {
      userProfileQuestions(status: $status, skip: $skip, first: $first, sortField: $sortField, sortOrder: $sortOrder) {
        totalNum
        questions { frontendId title titleSlug numSubmitted }
      }
    }
  `;
  while (true) {
    const d = await callWithRetry(
      () => callLeetCodeGraphql(session, query, { status: "ACCEPTED", skip, first, sortField: "LAST_SUBMITTED_AT", sortOrder: "DESCENDING" }),
      `userProfileQuestions(skip=${skip})`
    );
    const data = d?.userProfileQuestions;
    if (!data?.questions?.length) break;
    all.push(...data.questions);
    if (all.length >= data.totalNum) break;
    skip += first;
    await sleep(300);
  }
  return all;
}

async function fetchAllAcProblemsFromApi(session) {
  // 使用 REST API 而非 GraphQL submissionList 的原因：
  // 1. submissionList 只返回近期提交(约800条)，无法获取全部 AC 题目
  // 2. REST API /api/problems/all/ 返回用户所有题目的状态，包括 AC 的题目
  // 3. 该接口一次请求即可获取全部 441 道 AC 题目的基础信息
  console.log("Fetching all AC problems from API...");

  const response = await fetch(LEETCODE_API_URL, {
    headers: {
      cookie: `LEETCODE_SESSION=${session}`,
      "content-type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }

  const data = await response.json();
  const pairs = data?.stat_status_pairs || [];

  const acProblems = pairs
    .filter((p) => p.status === "ac")
    .map((p) => ({
      slug: p.stat?.question__title_slug,
      title: p.stat?.question__title,
      id: String(p.stat?.frontend_question_id || p.stat?.question_id),
      difficulty: p.difficulty?.level === 1 ? "Easy" : p.difficulty?.level === 3 ? "Hard" : "Medium",
    }))
    .filter((p) => p.slug);

  console.log(`Found ${acProblems.length} AC problems from API`);
  console.log(`  Total problems in database: ${pairs.length}`);
  console.log(`  AC Easy: ${data.ac_easy}, Medium: ${data.ac_medium}, Hard: ${data.ac_hard}`);

  return acProblems;
}

async function fetchProblemDetail(session, titleSlug) {
  const query = `
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        translatedTitle
        titleSlug
        difficulty
        topicTags {
          name
        }
      }
    }
  `;

  const data = await callWithRetry(
    () => callLeetCodeGraphql(session, query, { titleSlug }),
    `questionData(${titleSlug})`
  );

  const q = data?.question;
  if (!q) return null;

  // 中文标题获取策略：
  // GraphQL question 查询中的 translatedTitle 字段返回中文标题
  // 优先使用中文标题（需判断非空字符串），若不存在则回退到英文 title
  // 注意：部分题目可能没有中文翻译，此时 translatedTitle 为 null 或空字符串
  const title = q.translatedTitle?.trim() || q.title;

  return {
    id: String(q.questionFrontendId || q.questionId),
    title: title,
    slug: q.titleSlug,
    difficulty: q.difficulty,
    tags: (q.topicTags || []).map((t) => t.name).filter(Boolean),
  };
}

async function fetchSubmissionsForProblem(session, titleSlug) {
  const submissions = [];
  let offset = 0;

  const query = `
    query submissionList($offset: Int!, $limit: Int!, $slug: String!) {
      submissionList(offset: $offset, limit: $limit, questionSlug: $slug) {
        hasNext
        submissions {
          id
          statusDisplay
          lang
          timestamp
          runtime
          memory
          url
        }
      }
    }
  `;

  while (true) {
    const data = await callWithRetry(
      () =>
        callLeetCodeGraphql(session, query, {
          offset,
          limit: PAGE_SIZE,
          slug: titleSlug,
        }),
      `submissionList(${titleSlug}, ${offset})`
    );

    const list = data?.submissionList;
    const pageSubmissions = Array.isArray(list?.submissions) ? list.submissions : [];

    for (const sub of pageSubmissions) {
      submissions.push({
        id: sub.id,
        timestamp: toNumber(sub.timestamp),
        status: sub.statusDisplay,
        lang: sub.lang,
        runtime: sub.runtime,
        memory: sub.memory,
        url: sub.url,
      });
    }

    if (!list?.hasNext || pageSubmissions.length === 0) {
      break;
    }

    offset += PAGE_SIZE;
    await sleep(REQUEST_DELAY_MS);
  }

  return submissions;
}

async function fetchSubmissionCode(session, submissionId) {
  // 代码获取接口选择：
  // 1. GraphQL submissionDetails 接口限流极其严格，大量请求会被 403 拒绝
  // 2. REST API /api/submissions/{id}/ 更稳定，返回包含 code 字段的 JSON
  // 3. 经测试，该 REST 接口配合 1000ms 间隔可稳定获取全部代码
  const url = `https://leetcode.cn/api/submissions/${submissionId}/`;

  const fetchCode = async () => {
    const response = await fetch(url, {
      headers: {
        cookie: `LEETCODE_SESSION=${session}`,
        accept: "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`Code fetch failed with status ${response.status}`);
    }

    const data = await response.json();
    return data?.code || null;
  };

  // 添加重试机制，代码获取接口也可能限流
  return callWithRetry(fetchCode, `fetchSubmissionCode(${submissionId})`);
}

function getLatestAcSubmission(submissions) {
  const acSubmissions = submissions.filter(
    (s) => s.status === "Accepted"
  );
  if (acSubmissions.length === 0) return null;

  acSubmissions.sort((a, b) => b.timestamp - a.timestamp);
  return acSubmissions[0];
}

function getLanguageDisplayName(lang) {
  const langMap = {
    python3: "python",
    python: "python",
    cpp: "cpp",
    java: "java",
    javascript: "javascript",
    typescript: "typescript",
    golang: "go",
    go: "go",
    rust: "rust",
    c: "c",
    csharp: "csharp",
    php: "php",
    ruby: "ruby",
    swift: "swift",
    kotlin: "kotlin",
    scala: "scala",
    mysql: "mysql",
    mssql: "mssql",
    oraclesql: "oraclesql",
  };
  return langMap[lang?.toLowerCase()] || lang || "text";
}

function parseSubmissionRow(line) {
  const cells = line.split("|").slice(1, -1).map((cell) => cell.trim());
  if (cells.length !== 6) {
    throw new Error(`Invalid submission row: ${line}`);
  }

  const [id, submittedAt, lang, status, runtime, memory] = cells;
  return {
    id,
    timestamp: parseExportedDateTime(submittedAt),
    lang,
    status,
    runtime: runtime === "N/A" ? null : runtime,
    memory: memory === "N/A" ? null : memory,
    url: null,
  };
}

function parseProblemSection(section) {
  const lines = section.trim().split(/\r?\n/);
  const headerMatch = lines[0]?.match(/^## (.+) \(`([^`]+)`\)$/);
  if (!headerMatch) {
    throw new Error(`Invalid problem header: ${lines[0] || "(empty)"}`);
  }

  const [, idAndTitle, slug] = headerMatch;
  const separatorIndex = idAndTitle.lastIndexOf(". ");
  if (separatorIndex === -1) {
    throw new Error(`Invalid problem header body: ${lines[0]}`);
  }

  const id = idAndTitle.slice(0, separatorIndex).trim();
  const title = idAndTitle.slice(separatorIndex + 2).trim();
  const metadata = new Map();

  let index = 1;
  while (index < lines.length && lines[index] !== "### 提交记录") {
    const line = lines[index];
    if (line.startsWith("- ")) {
      const separator = line.indexOf("：");
      if (separator !== -1) {
        metadata.set(line.slice(2, separator), line.slice(separator + 1).trim());
      }
    }
    index += 1;
  }

  if (lines[index] !== "### 提交记录") {
    throw new Error(`Missing submission section for ${slug}`);
  }

  index += 1;
  while (index < lines.length && lines[index] === "") {
    index += 1;
  }

  let submissions = [];
  if (lines[index] === "暂无提交记录") {
    index += 1;
  } else {
    if (!lines[index]?.startsWith("| 提交ID |") || !lines[index + 1]?.startsWith("| --- |")) {
      throw new Error(`Invalid submission table for ${slug}`);
    }
    index += 2;
    const rows = [];
    while (index < lines.length && lines[index].startsWith("|")) {
      rows.push(lines[index]);
      index += 1;
    }
    submissions = rows.map(parseSubmissionRow);
  }

  const codeHeadingIndex = lines.indexOf("### 最近一次 AC 代码", index);
  if (codeHeadingIndex === -1) {
    throw new Error(`Missing latest AC code section for ${slug}`);
  }

  index = codeHeadingIndex + 1;
  while (index < lines.length && lines[index] === "") {
    index += 1;
  }

  let code = null;
  if (lines[index] !== "（暂无 AC 代码）") {
    if (!lines[index]?.startsWith("```")) {
      throw new Error(`Invalid code block for ${slug}`);
    }
    index += 1;
    const codeLines = [];
    while (index < lines.length && lines[index] !== "```") {
      codeLines.push(lines[index]);
      index += 1;
    }
    if (lines[index] !== "```") {
      throw new Error(`Unclosed code block for ${slug}`);
    }
    code = codeLines.join("\n").trim() || null;
  }

  const latestAc = getLatestAcSubmission(submissions);
  const latestSubmissionTime = submissions.length > 0
    ? Math.max(...submissions.map((submission) => submission.timestamp).filter(Boolean))
    : null;
  const tagsValue = metadata.get("标签") || "无";
  const totalSubmissions = toNumber(metadata.get("总提交次数")) ?? submissions.length;

  return {
    id,
    title,
    slug,
    difficulty: metadata.get("难度") || "Unknown",
    tags: tagsValue === "无" ? [] : tagsValue.split(", ").filter(Boolean),
    submissions,
    latestAc,
    code,
    totalSubmissions,
    latestSubmissionTime: parseExportedDateTime(metadata.get("最近提交时间")) ?? latestSubmissionTime,
  };
}

function parseMarkdownExport(content) {
  const generatedAtMatch = content.match(/^- 生成时间：(.*)$/m);
  if (!generatedAtMatch) {
    throw new Error("Missing generated time in markdown export");
  }

  const generatedAt = parseExportedDateTime(generatedAtMatch[1].trim());
  const sections = content
    .split(/(?=^## )/m)
    .slice(1)
    .map((section) => section.trim())
    .filter(Boolean);

  return {
    generatedAt,
    problemsData: sections.map(parseProblemSection),
  };
}

function buildCachePayload({ acProblems, problemsData, generatedAt = null, output = null, source = null }) {
  return {
    acProblems,
    problemsData,
    generatedAt,
    output,
    source,
  };
}

async function fetchProblemData(session, problemInfo, skipCode = false) {
  // 题目详情和提交记录获取独立，避免一个失败导致整个题目失败
  let detail = null;
  let submissions = [];

  try {
    detail = await fetchProblemDetail(session, problemInfo.slug);
  } catch (error) {
    console.log(`  Warning: Failed to fetch problem detail for ${problemInfo.title}: ${error.message}`);
    // 使用 API 返回的基础信息作为回退
    detail = {
      id: problemInfo.id,
      title: problemInfo.title,
      slug: problemInfo.slug,
      difficulty: problemInfo.difficulty,
      tags: [],
    };
  }

  try {
    submissions = await fetchSubmissionsForProblem(session, problemInfo.slug);
  } catch (error) {
    console.log(`  Warning: Failed to fetch submissions for ${problemInfo.title}: ${error.message}`);
    // 提交记录获取失败，保留空数组
  }

  const latestAc = getLatestAcSubmission(submissions);

  let code = null;
  if (latestAc && !skipCode) {
    try {
      code = await fetchSubmissionCode(session, latestAc.id);
      await sleep(CODE_FETCH_DELAY_MS);
    } catch (e) {
      // 代码获取失败，记录但不阻断流程
      console.log(`  Warning: Failed to fetch code for submission ${latestAc.id}: ${e.message}`);
    }
  }

  return {
    id: problemInfo.id,
    title: detail?.title || problemInfo.title,
    slug: problemInfo.slug,
    difficulty: detail?.difficulty || problemInfo.difficulty,
    tags: detail?.tags || [],
    submissions,
    latestAc,
    code,
    totalSubmissions: submissions.length,
    latestSubmissionTime: submissions.length > 0
      ? Math.max(...submissions.map((s) => s.timestamp).filter(Boolean))
      : null,
  };
}

function renderSubmissionTable(submissions) {
  if (submissions.length === 0) {
    return "暂无提交记录";
  }

  const rows = submissions
    .sort((a, b) => b.timestamp - a.timestamp)
    .map((s) => {
      const time = formatDateTime(s.timestamp);
      const runtime = s.runtime || "N/A";
      const memory = s.memory || "N/A";
      return `| ${s.id} | ${time} | ${getLanguageDisplayName(s.lang)} | ${s.status} | ${runtime} | ${memory} |`;
    });

  return [
    "| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |",
    "| --- | --- | --- | --- | --- | --- |",
    ...rows,
  ].join("\n");
}

function renderProblemSection(problem) {
  const difficulty = problem.difficulty || "Unknown";
  const tags = problem.tags || [];
  const tagsStr = tags.length > 0 ? tags.join(", ") : "无";
  const problemUrl = `https://leetcode.cn/problems/${problem.slug}/`;

  const lines = [
    `## ${problem.id}. ${problem.title} (\`${problem.slug}\`)`,
    "",
    `- 题目链接：${problemUrl}`,
    `- 难度：${difficulty}`,
    `- 标签：${tagsStr}`,
    `- 总提交次数：${problem.totalSubmissions}`,
    `- 最近提交时间：${formatDateTime(problem.latestSubmissionTime)}`,
    "",
    "### 提交记录",
    renderSubmissionTable(problem.submissions),
    "",
  ];

  if (problem.code) {
    const lang = getLanguageDisplayName(problem.latestAc?.lang);
    lines.push(
      "### 最近一次 AC 代码",
      "",
      `\`\`\`${lang}`,
      problem.code.trim(),
      "```",
      ""
    );
  } else {
    lines.push(
      "### 最近一次 AC 代码",
      "",
      "（暂无 AC 代码）",
      ""
    );
  }

  return lines.join("\n");
}

function renderMarkdown(problemsData, stats, generatedAt = new Date()) {
  const formatStatsDate = (d) => d.toLocaleString("zh-CN", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }) + " CST";

  const totalSubmissions = stats.totalSubmissions;

  const sections = [
    "# LeetCode 提交汇总",
    "",
    `- 生成时间：${formatStatsDate(generatedAt)}`,
    `- AC 题目数：${problemsData.length}`,
    `- 总提交数：${totalSubmissions}`,
    "",
  ];

  const isNumericId = (value) => /^\d+$/.test(value);
  const sortedProblems = [...problemsData].sort((a, b) => {
    const aNumeric = isNumericId(a.id);
    const bNumeric = isNumericId(b.id);

    if (aNumeric && bNumeric) {
      return Number(a.id) - Number(b.id);
    }
    if (aNumeric) return -1;
    if (bNumeric) return 1;
    return a.id.localeCompare(b.id, "zh-Hans-CN");
  });

  for (const problem of sortedProblems) {
    sections.push(renderProblemSection(problem));
  }

  return sections.join("\n");
}

// 保存缓存
async function saveCache(cache) {
  await mkdir(CACHE_DIR, { recursive: true });
  await writeFile(CACHE_FILE, JSON.stringify(cache, null, 2), "utf8");
}

// 加载缓存
async function loadCache() {
  try {
    const content = await readFile(CACHE_FILE, "utf8");
    const cache = JSON.parse(content);
    // 验证缓存结构完整性
    if (!cache || typeof cache !== "object" || !Array.isArray(cache.acProblems)) {
      console.log("Cache file corrupted or invalid format, ignoring...");
      return null;
    }
    return cache;
  } catch (error) {
    // 文件不存在或解析失败，返回 null 表示无有效缓存
    return null;
  }
}

async function main() {
  const { output, skipCode, resume, verify, incremental } = parseArgs(process.argv.slice(2));

  if (!process.env.LEETCODE_SESSION) {
    throw new Error("LEETCODE_SESSION is not set");
  }

  const session = process.env.LEETCODE_SESSION;

  if (incremental) {
    console.log("=== Incremental mode ===\n");

    const cache = await loadCache();
    let baseline;
    try {
      const previousExport = await readFile(output, "utf8");
      const parsedExport = parseMarkdownExport(previousExport);
      const cacheMatchesOutput = cache?.output === output && toNumber(cache.generatedAt) === parsedExport.generatedAt;
      baseline = cacheMatchesOutput && Array.isArray(cache?.problemsData)
        ? { generatedAt: parsedExport.generatedAt, problemsData: cache.problemsData }
        : parsedExport;
    } catch (error) {
      if (error?.code === "ENOENT") {
        throw new Error(`Output file not found: ${output}. Run a full export first.`);
      }
      throw new Error(`Failed to parse existing export ${output}: ${error.message}`);
    }

    console.log(`Loaded baseline export from ${output}`);
    console.log(`  Generated at: ${formatDateTime(baseline.generatedAt)}`);
    console.log(`  Baseline problems: ${baseline.problemsData.length}\n`);

    const baselineBySlug = new Map(baseline.problemsData.map((problem) => [problem.slug, problem]));

    const currentAcProblems = await fetchAllAcProblemsFromApi(session);
    const currentProblemBySlug = new Map(currentAcProblems.map((problem) => [problem.slug, problem]));

    console.log("Fetching server-side submission counts...");
    const serverQuestions = await fetchServerSubmitCounts(session);
    const serverCountBySlug = new Map(serverQuestions.map((question) => [question.titleSlug, question.numSubmitted]));

    const problemsToRefresh = [];
    let newAcProblems = 0;
    let countMismatches = 0;
    let serverCountMissing = 0;

    for (const problemInfo of currentAcProblems) {
      const localProblem = baselineBySlug.get(problemInfo.slug);
      const serverCount = serverCountBySlug.get(problemInfo.slug);

      if (!localProblem) {
        problemsToRefresh.push(problemInfo);
        newAcProblems += 1;
        continue;
      }

      if (serverCount === undefined) {
        problemsToRefresh.push(problemInfo);
        serverCountMissing += 1;
        continue;
      }

      if ((localProblem.totalSubmissions || 0) !== serverCount) {
        problemsToRefresh.push(problemInfo);
        countMismatches += 1;
      }
    }

    const removedProblems = baseline.problemsData.filter((problem) => !currentProblemBySlug.has(problem.slug)).length;
    console.log(`Current AC problems: ${currentAcProblems.length}`);
    console.log(`  New AC problems: ${newAcProblems}`);
    console.log(`  Submission count changed: ${countMismatches}`);
    console.log(`  Missing server counts: ${serverCountMissing}`);
    console.log(`  Removed from current AC list: ${removedProblems}`);
    console.log(`  Problems to refresh: ${problemsToRefresh.length}\n`);

    const refreshedBySlug = new Map();
    const failedRefreshes = [];

    if (problemsToRefresh.length > 0) {
      console.log(`Refreshing changed problems with concurrency ${CONCURRENCY}...\n`);
      for (let i = 0; i < problemsToRefresh.length; i += CONCURRENCY) {
        const chunk = problemsToRefresh.slice(i, i + CONCURRENCY);
        const refreshedChunk = await Promise.all(chunk.map(async (problemInfo, chunkIndex) => {
          const progress = i + chunkIndex + 1;
          console.log(`[${progress}/${problemsToRefresh.length}] Refreshing: ${problemInfo.title}...`);
          try {
            return await fetchProblemData(session, problemInfo, skipCode);
          } catch (error) {
            failedRefreshes.push(problemInfo.slug);
            console.log(`  -> Failed: ${error.message}`);
            return null;
          }
        }));

        for (const problem of refreshedChunk.filter(Boolean)) {
          refreshedBySlug.set(problem.slug, problem);
        }
        await sleep(REQUEST_DELAY_MS * 2);
      }
    }

    if (failedRefreshes.length > 0) {
      throw new Error(`Incremental refresh failed for ${failedRefreshes.length} problems: ${failedRefreshes.join(", ")}`);
    }

    const problemsData = currentAcProblems
      .map((problemInfo) => refreshedBySlug.get(problemInfo.slug) || baselineBySlug.get(problemInfo.slug))
      .filter(Boolean);

    const exportedAt = new Date();
    const generatedAt = Math.floor(exportedAt.getTime() / 1000);
    await saveCache(buildCachePayload({
      acProblems: currentAcProblems,
      problemsData,
      generatedAt,
      output,
      source: "incremental",
    }));

    const totalSubmissions = problemsData.reduce((sum, problem) => sum + (problem.totalSubmissions || 0), 0);
    const markdown = renderMarkdown(problemsData, { totalSubmissions }, exportedAt);
    await writeFile(output, markdown, "utf8");

    console.log(`\nExported to ${output}`);
    console.log(`Total submissions: ${totalSubmissions}`);
    return;
  }

  // ── verify 模式 ─────────────────────────────────────────────────────────────
  // 用 userProfileQuestions API 拿服务端每题的 numSubmitted，
  // 与缓存按 slug 对比，只重新抓取有差异的题目，最后重新生成 markdown。
  if (verify) {
    console.log("=== Verify mode ===\n");

    const cache = await loadCache();
    if (!cache?.problemsData?.length) {
      throw new Error("No cache found. Run without --verify first to build the cache.");
    }

    const problems = cache.problemsData;
    const slugToIdx = {};
    for (let i = 0; i < problems.length; i++) {
      slugToIdx[problems[i].slug] = i;
    }

    console.log("Fetching server-side submission counts...");
    const serverQuestions = await fetchServerSubmitCounts(session);
    console.log(`Server: ${serverQuestions.length} AC problems\n`);

    const toRetry = [];
    for (const sq of serverQuestions) {
      const idx = slugToIdx[sq.titleSlug];
      if (idx === undefined) {
        console.log(`  WARNING: ${sq.titleSlug} not in cache`);
        continue;
      }
      const ours = problems[idx].totalSubmissions || 0;
      if (ours !== sq.numSubmitted) {
        toRetry.push({ idx, slug: sq.titleSlug, title: sq.title, serverCount: sq.numSubmitted, ourCount: ours });
      }
    }

    console.log(`Found ${toRetry.length} problems with submission count mismatch\n`);

    if (toRetry.length > 0) {
      const VERIFY_CONCURRENCY = 2;
      let fixed = 0;

      for (let b = 0; b < toRetry.length; b += VERIFY_CONCURRENCY) {
        const chunk = toRetry.slice(b, b + VERIFY_CONCURRENCY);
        await Promise.all(chunk.map(async (item, chunkIdx) => {
          const { idx, slug, title, serverCount, ourCount } = item;
          console.log(`[${b + chunkIdx + 1}/${toRetry.length}] ${title} (${slug}): server=${serverCount} ours=${ourCount}`);
          try {
            // 使用 problemsData 里已有的基础信息作为 problemInfo
            const problemInfo = {
              slug,
              title,
              id: problems[idx].id,
              difficulty: problems[idx].difficulty,
            };
            const data = await fetchProblemData(session, problemInfo, skipCode);
            problems[idx] = data;
            fixed++;
            console.log(`  -> Fixed: ${data.totalSubmissions} submissions`);
          } catch (e) {
            console.log(`  -> Failed: ${e.message}`);
          }
        }));
        await saveCache(cache);
        await sleep(REQUEST_DELAY_MS * 2);
      }

      console.log(`\nFixed ${fixed}/${toRetry.length}`);
    }

    // 统计并生成 markdown
    const total = problems.reduce((s, p) => s + (p.totalSubmissions || 0), 0);
    console.log(`\nTotal submissions: ${total}`);
    const exportedAt = new Date();
    const generatedAt = Math.floor(exportedAt.getTime() / 1000);
    await saveCache(buildCachePayload({
      acProblems: cache.acProblems,
      problemsData: problems,
      generatedAt,
      output,
      source: "verify",
    }));
    const markdown = renderMarkdown(problems, { totalSubmissions: total }, exportedAt);
    await writeFile(output, markdown, "utf8");
    console.log(`Exported to ${output}`);
    return;
  }

  // ── 正常抓取模式 ─────────────────────────────────────────────────────────────
  console.log(`Skip code fetching: ${skipCode}\n`);

  // 尝试加载缓存
  // 缓存机制设计：
  // 1. 因抓取 441 题约需 20-30 分钟，中途失败代价高，故引入断点续传
  // 2. 每完成 10 道题自动保存缓存，避免重复工作
  // 3. 使用 --resume 或 -r 参数从缓存继续，否则重新抓取
  // 4. 缓存包含题目列表和已抓取数据，存储为 JSON 格式
  let cache = await loadCache();
  let acProblems;
  let problemsData = [];
  let startIndex = 0;

  if (cache && cache.acProblems && cache.problemsData) {
    console.log(`Found cache: ${cache.problemsData.length}/${cache.acProblems.length} problems fetched`);
    
    if (resume) {
      console.log("Resuming from cache...");
      acProblems = cache.acProblems;
      problemsData = cache.problemsData;
      startIndex = problemsData.length;
    } else {
      console.log("To resume from cache, use --resume or -r flag");
      console.log("Starting fresh fetch...\n");
      acProblems = await fetchAllAcProblemsFromApi(session);
    }
  } else {
    acProblems = await fetchAllAcProblemsFromApi(session);
  }

  console.log(`\nTotal AC problems: ${acProblems.length}`);
  console.log(`Already fetched: ${problemsData.length}`);
  console.log(`Remaining: ${acProblems.length - startIndex}`);
  console.log(`Concurrency: ${CONCURRENCY}\n`);

  // 获取剩余题目的详细数据
  const remainingProblems = acProblems.slice(startIndex);

  if (remainingProblems.length > 0) {
    console.log(`Fetching ${remainingProblems.length} problems with concurrency ${CONCURRENCY}...\n`);

    // 预分配数组，按索引写入，避免并发 push 导致 problemsData 与 acProblems 顺序错位
    const fetchedData = new Array(remainingProblems.length).fill(null);
    let completed = 0;

    const processor = async (problemInfo, idx) => {
      const actualIndex = startIndex + idx;
      console.log(`[${actualIndex + 1}/${acProblems.length}] Fetching: ${problemInfo.title}...`);

      try {
        const data = await fetchProblemData(session, problemInfo, skipCode);
        // 按索引写入，保证顺序与 acProblems 一致
        fetchedData[idx] = data;
        completed++;

        // 每完成 10 道题保存一次缓存
        // 注意：fetchedData 中仍有 null（并发中尚未完成的任务），filter(Boolean) 确保只保存已完成的数据
        // 极端情况下（进程崩溃），已完成但因 null 空位被截断的题目不会写入缓存，需重抓
        if (completed % 10 === 0) {
          const currentData = [...problemsData, ...fetchedData.filter(Boolean)];
          await saveCache(buildCachePayload({ acProblems, problemsData: currentData, source: "partial" }));
          console.log(`  -> Saved cache (${currentData.length}/${acProblems.length})`);
        }

        return data;
      } catch (error) {
        console.error(`  -> Failed: ${error.message}`);
        return null;
      }
    };

    // 使用并发控制，分块处理
    const chunkSize = CONCURRENCY;
    for (let i = 0; i < remainingProblems.length; i += chunkSize) {
      const chunk = remainingProblems.slice(i, i + chunkSize);
      await Promise.all(chunk.map((p, idx) => processor(p, i + idx)));
      await sleep(REQUEST_DELAY_MS * 2);
    }

    // 合并已有数据与新抓取数据（过滤掉失败的 null）
    problemsData = [...problemsData, ...fetchedData.filter(Boolean)];
  }

  // 保存最终缓存
  const exportedAt = new Date();
  const generatedAt = Math.floor(exportedAt.getTime() / 1000);
  await saveCache(buildCachePayload({
    acProblems,
    problemsData,
    generatedAt,
    output,
    source: resume ? "resume" : "full",
  }));

  console.log(`\nSuccessfully fetched ${problemsData.length}/${acProblems.length} problems`);

  // 统计信息
  let totalSubmissions = 0;
  let codeSuccessCount = 0;
  for (const p of problemsData) {
    totalSubmissions += p.totalSubmissions;
    if (p.code) codeSuccessCount++;
  }

  const stats = { totalSubmissions };
  const markdown = renderMarkdown(problemsData, stats, exportedAt);

  await writeFile(output, markdown, "utf8");
  console.log(`\nExported to ${output}`);
  console.log(`Total submissions: ${totalSubmissions}`);
  console.log(`Code fetched: ${codeSuccessCount}/${problemsData.length} (${Math.round(codeSuccessCount / problemsData.length * 100)}%)`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
