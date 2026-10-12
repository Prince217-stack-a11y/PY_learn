"""A small demo package built for the s05 TodoWrite example.

It exposes a few dependency-free helpers for shaping and summarizing
todo-style task lists::

    >>> from demo_pkg import slugify, render_todo
    >>> slugify("Write Docs!")
    'write-docs'
    >>> render_todo({"content": "Write docs", "status": "completed"})
    '[x] Write docs'
"""

from .utils import (
    VALID_STATUSES,
    count_by_status,
    render_todo,
    slugify,
)

__version__ = "0.1.0"

__all__ = [
    "VALID_STATUSES",
    "count_by_status",
    "render_todo",
    "slugify",
    "__version__",
]
