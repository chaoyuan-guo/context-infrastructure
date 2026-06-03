import yaml
import re
from typing import List, Dict, Any
from .models import Chunk


class SessionUserChunker:
    """Extract user messages from agent_traces session files, anchored with preceding AI context.

    Each file's content is parsed for user turns (text after each **chaoyuan** marker).
    For rounds 2+, the preceding assistant response's first N chars are prepended as context
    anchor, so the embedding reflects what the user is responding to — not just the user's
    short message in isolation.
    """

    def __init__(self, context_chars: int = 200):
        self.context_chars = context_chars
        self._md_chunker = MarkdownChunker()

    def chunk(self, file_path: str, content: str) -> List[Chunk]:
        metadata, body = self._md_chunker.parse_yaml_frontmatter(content)

        rounds = re.split(r'\n(?=## Round \d+)', body)
        chunks: List[Chunk] = []
        prev_assistant = ""

        for round_text in rounds:
            if not re.match(r'## Round', round_text):
                continue

            round_match = re.match(r'## Round (\d+)', round_text)
            round_num = round_match.group(1) if round_match else "?"

            user_match = re.search(
                r'\*\*chaoyuan[^*]*\*\*.*?\n+(.*?)(?=\n\*\*OpenCode|\Z)',
                round_text, re.DOTALL
            )
            if not user_match:
                continue

            user_text = user_match.group(1).strip()
            if not user_text:
                continue

            assistant_match = re.search(
                r'\*\*OpenCode[^*]*\*\*.*?\n+(.*?)(?=\n## Round|\Z)',
                round_text, re.DOTALL
            )
            assistant_text = assistant_match.group(1).strip() if assistant_match else ""

            if prev_assistant:
                ctx = prev_assistant[:self.context_chars]
                chunk_text = f"[上文: {ctx}]\n\n{user_text}"
            else:
                chunk_text = user_text

            chunks.append(Chunk(
                id=f"{file_path}:u{round_num}",
                text=chunk_text,
                source_file=file_path,
                header=f"## Round {round_num}",
                position=(0, 0),
                metadata={**metadata, 'chunk_type': 'user_turn'}
            ))

            prev_assistant = assistant_text

        return chunks


class MarkdownChunker:
    def __init__(self, max_chunk_size: int = 1000, overlap: int = 100):
        self.max_chunk_size = max_chunk_size
        self.overlap = overlap

    def parse_yaml_frontmatter(self, content: str) -> tuple[Dict[str, Any], str]:
        """提取 YAML 元数据和正文。"""
        if content.startswith('---'):
            parts = re.split(r'^---', content, flags=re.MULTILINE)
            if len(parts) >= 3:
                try:
                    metadata = yaml.safe_load(parts[1])
                    body = '---'.join(parts[2:]).strip()
                    return metadata or {}, body
                except yaml.YAMLError:
                    pass
        return {}, content.strip()

    def chunk(self, file_path: str, content: str) -> List[Chunk]:
        """按标题分块并保留元数据。"""
        metadata, body = self.parse_yaml_frontmatter(content)
        chunks = []
        
        lines = body.split('\n')
        current_header = ""
        current_chunk_lines = []
        chunk_idx = 0
        start_line = 1 # TODO: accurately track line numbers if needed

        for i, line in enumerate(lines, 1):
            if line.startswith('#'):
                # Save previous chunk if it exists
                if current_chunk_lines:
                    chunks.append(Chunk(
                        id=f"{file_path}:{chunk_idx}",
                        text="\n".join(current_chunk_lines),
                        source_file=file_path,
                        header=current_header,
                        position=(start_line, i-1),
                        metadata=metadata
                    ))
                    chunk_idx += 1
                
                current_header = line
                current_chunk_lines = [line]
                start_line = i
            else:
                current_chunk_lines.append(line)
                
                # Split if chunk is too large
                if len("\n".join(current_chunk_lines)) > self.max_chunk_size:
                    chunks.append(Chunk(
                        id=f"{file_path}:{chunk_idx}",
                        text="\n".join(current_chunk_lines),
                        source_file=file_path,
                        header=current_header,
                        position=(start_line, i),
                        metadata=metadata
                    ))
                    chunk_idx += 1
                    # Start next chunk with header for context
                    current_chunk_lines = [current_header] if current_header else []
                    start_line = i

        # Final chunk
        if current_chunk_lines:
            chunks.append(Chunk(
                id=f"{file_path}:{chunk_idx}",
                text="\n".join(current_chunk_lines),
                source_file=file_path,
                header=current_header,
                position=(start_line, len(lines)),
                metadata=metadata
            ))
            
        return chunks
