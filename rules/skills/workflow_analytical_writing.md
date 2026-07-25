# 分析写作兼容入口

## 状态

这个文件是本地兼容层，不再是独立 workflow。upstream 已将旧版分析写作工作流分为两部分：

- 分析视角：[`reference_writing_thesis_catalog.md`](./reference_writing_thesis_catalog.md)
- 外部成文与验收：[`workflow_external_writing.md`](./workflow_external_writing.md)

保留这个路径，是为了让尚未迁移的本地 workflow 仍能正常路由。新 workflow 不应再引用本文件。

## 路由

1. 面向陌生读者或公开发布的分析文章：先读 thesis catalog，再执行 external writing workflow。
2. 面向用户本人或共享上下文协作者的 memo：使用 [`workflow_internal_writing.md`](./workflow_internal_writing.md)。
3. 事实采集与外部验证尚未完成时：先执行 [`workflow_deep_research_survey.md`](./workflow_deep_research_survey.md) Phase 1-3。
