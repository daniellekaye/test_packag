"""
test_project: Test package for CSCI 4050 (Software Engineering), Fall 2025
"""

from __future__ import annotations

from importlib.metadata import version

__all__ = ("__version__",)
__version__ = version(__name__)
