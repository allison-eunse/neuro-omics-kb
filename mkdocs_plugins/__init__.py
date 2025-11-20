"""MkDocs plugins for code citations and custom formatting."""

# Export the plugin class for MkDocs discovery
from .code_citations import CodeCitationsPlugin

__all__ = ["CodeCitationsPlugin"]
