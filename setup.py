"""Setup script for MkDocs plugins."""

from setuptools import find_packages, setup

setup(
    name="neuro-omics-kb-plugins",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "code_citations = mkdocs_plugins.code_citations:CodeCitationsPlugin",
        ],
    },
)
