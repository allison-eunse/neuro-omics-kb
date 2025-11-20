"""
MkDocs plugin to process custom code citation format: ```startLine:endLine:filepath
Extracts language from file extension and formats code blocks with file path display.
"""

import re
from pathlib import Path

from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

# Map file extensions to Pygments language names
EXTENSION_TO_LANG = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".jsx": "jsx",
    ".tsx": "tsx",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".h": "c",
    ".hpp": "cpp",
    ".cs": "csharp",
    ".go": "go",
    ".rs": "rust",
    ".rb": "ruby",
    ".php": "php",
    ".swift": "swift",
    ".kt": "kotlin",
    ".scala": "scala",
    ".sh": "bash",
    ".bash": "bash",
    ".zsh": "bash",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".json": "json",
    ".xml": "xml",
    ".html": "html",
    ".css": "css",
    ".scss": "scss",
    ".sass": "sass",
    ".less": "less",
    ".sql": "sql",
    ".r": "r",
    ".R": "r",
    ".m": "matlab",
    ".jl": "julia",
    ".md": "markdown",
    ".tex": "latex",
    ".toml": "toml",
    ".ini": "ini",
    ".cfg": "ini",
    ".conf": "ini",
    ".dockerfile": "dockerfile",
    ".dockerignore": "dockerfile",
    ".makefile": "makefile",
    ".mk": "makefile",
}


def detect_language(filepath: str) -> str:
    """Detect language from file extension."""
    path = Path(filepath)
    ext = path.suffix.lower()
    return EXTENSION_TO_LANG.get(ext, "text")


def process_code_citations(content: str) -> str:
    """
    Process code citation format: ```startLine:endLine:filepath
    Converts to: ```language
    And adds file path as a comment or in a data attribute.
    """
    # Pattern: ```startLine:endLine:filepath
    pattern = r"```(\d+):(\d+):([^\n]+)\n"

    def replace_match(match):
        start_line = match.group(1)
        end_line = match.group(2)
        filepath = match.group(3).strip()
        language = detect_language(filepath)

        # Replace with standard format: ```language
        # pymdownx.superfences supports title attribute for file paths
        return f'```{language} title="{filepath} (lines {start_line}-{end_line})"\n'

    content = re.sub(pattern, replace_match, content)
    return content


class CodeCitationsPlugin(BasePlugin):
    """MkDocs plugin to process custom code citation format."""

    def on_page_markdown(self, markdown: str, page: Page, **kwargs) -> str:
        """Process markdown to handle custom code citation format."""
        return process_code_citations(markdown)
