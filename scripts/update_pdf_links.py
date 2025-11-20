#!/usr/bin/env python3
"""
Update all PDF links in markdown files to use GitHub raw URLs instead of relative paths.
This allows PDFs to be served from the repository without being copied to the built site.
"""

import re
from pathlib import Path

# GitHub repository details
REPO_OWNER = "allison-eunse"
REPO_NAME = "neuro-omics-kb"
BRANCH = "main"
BASE_RAW_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/docs"


def update_pdf_links(content: str, file_path: Path) -> str:
    """Replace relative PDF links with GitHub raw URLs."""

    # Pattern 1: Full path in markdown link [text](generated/kb_curated/papers-pdf/file.pdf)
    pattern1 = re.compile(
        r"(\[([^\]]+)\]\(generated/kb_curated/papers-pdf/([^)]+\.pdf)\))", re.IGNORECASE
    )

    def replace_full_path(match):
        link_text = match.group(2)
        pdf_file = match.group(3)
        raw_url = f"{BASE_RAW_URL}/generated/kb_curated/papers-pdf/{pdf_file}"
        return f"[{link_text}]({raw_url})"

    # Pattern 2: Relative path with ../ in markdown link
    # [text](../../generated/kb_curated/papers-pdf/file.pdf)
    pattern2 = re.compile(
        r"(\[([^\]]+)\]\(\.\./\.\./generated/kb_curated/papers-pdf/([^)]+\.pdf)\))", re.IGNORECASE
    )

    def replace_relative_up(match):
        link_text = match.group(2)
        pdf_file = match.group(3)
        raw_url = f"{BASE_RAW_URL}/generated/kb_curated/papers-pdf/{pdf_file}"
        return f"[{link_text}]({raw_url})"

    # Pattern 3: Relative path in markdown link [text](papers-pdf/file.pdf)
    pattern3 = re.compile(r"(\[([^\]]+)\]\(papers-pdf/([^)]+\.pdf)\))", re.IGNORECASE)

    def replace_relative_path(match):
        link_text = match.group(2)
        pdf_file = match.group(3)
        raw_url = f"{BASE_RAW_URL}/generated/kb_curated/papers-pdf/{pdf_file}"
        return f"[{link_text}]({raw_url})"

    # Pattern 4: Bare PDF path (generated/kb_curated/papers-pdf/file.pdf) - not in markdown link
    pattern4 = re.compile(r"\(generated/kb_curated/papers-pdf/([^)]+\.pdf)\)", re.IGNORECASE)

    def replace_bare_full(match):
        pdf_file = match.group(1)
        raw_url = f"{BASE_RAW_URL}/generated/kb_curated/papers-pdf/{pdf_file}"
        return f"({raw_url})"

    # Pattern 5: Bare relative PDF path with ../ (../../generated/kb_curated/papers-pdf/file.pdf)
    pattern5 = re.compile(
        r"\(\.\./\.\./generated/kb_curated/papers-pdf/([^)]+\.pdf)\)", re.IGNORECASE
    )

    def replace_bare_relative_up(match):
        pdf_file = match.group(1)
        raw_url = f"{BASE_RAW_URL}/generated/kb_curated/papers-pdf/{pdf_file}"
        return f"({raw_url})"

    # Pattern 6: Bare relative PDF path (papers-pdf/file.pdf)
    pattern6 = re.compile(r"\(papers-pdf/([^)]+\.pdf)\)", re.IGNORECASE)

    def replace_bare_relative(match):
        pdf_file = match.group(1)
        raw_url = f"{BASE_RAW_URL}/generated/kb_curated/papers-pdf/{pdf_file}"
        return f"({raw_url})"

    # Apply all patterns
    content = pattern1.sub(replace_full_path, content)
    content = pattern2.sub(replace_relative_up, content)
    content = pattern3.sub(replace_relative_path, content)
    content = pattern4.sub(replace_bare_full, content)
    content = pattern5.sub(replace_bare_relative_up, content)
    content = pattern6.sub(replace_bare_relative, content)

    return content


def process_file(file_path: Path) -> bool:
    """Process a single markdown file and update PDF links."""
    try:
        content = file_path.read_text(encoding="utf-8")
        updated_content = update_pdf_links(content, file_path)

        if content != updated_content:
            file_path.write_text(updated_content, encoding="utf-8")
            print(f"Updated: {file_path}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Find and update all markdown files in docs/ directory."""
    docs_dir = Path(__file__).parent.parent / "docs"

    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        return

    markdown_files = list(docs_dir.rglob("*.md"))
    updated_count = 0

    for md_file in markdown_files:
        if process_file(md_file):
            updated_count += 1

    print(f"\nProcessed {len(markdown_files)} markdown files")
    print(f"Updated {updated_count} files with PDF links")


if __name__ == "__main__":
    main()
