"""Dependency-free helpers for working with todo-style task lists."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

_STATUS_MARKERS: dict[str, str] = {
    "pending": "[ ]",
    "in_progress": "[>]",
    "completed": "[x]",
}

#: The statuses a todo may have, in display order (single source of truth).
VALID_STATUSES: tuple[str, ...] = tuple(_STATUS_MARKERS)


def slugify(text: str) -> str:
    """Convert ``text`` into a lowercase, hyphen-separated slug.

    Any run of characters that are not letters or digits collapses into a
    single ``-``, and leading/trailing hyphens are removed.

    Args:
        text: The string to slugify.

    Returns:
        The slug, or an empty string if ``text`` holds no letters or digits.

    Examples:
        >>> slugify("Write Docs!")
        'write-docs'
        >>> slugify("  ---  ")
        ''
    """
    parts: list[str] = []
    for char in text.lower():
        if char.isalnum():
            parts.append(char)
        elif parts and parts[-1] != "-":
            parts.append("-")
    return "".join(parts).strip("-")


def count_by_status(todos: Iterable[Mapping[str, str]]) -> dict[str, int]:
    """Count how many todos have each status.

    Args:
        todos: An iterable of mappings, each with a ``status`` key.

    Returns:
        A mapping covering every value in :data:`VALID_STATUSES`, even when
        its count is zero.

    Raises:
        ValueError: If a todo is missing a ``status`` or has an unknown one.

    Examples:
        >>> count_by_status([{"status": "pending"}, {"status": "pending"}])
        {'pending': 2, 'in_progress': 0, 'completed': 0}
    """
    counts: dict[str, int] = dict.fromkeys(VALID_STATUSES, 0)
    for index, todo in enumerate(todos):
        status = todo.get("status")
        if status not in counts:
            raise ValueError(f"todos[{index}] has invalid status {status!r}")
        counts[status] += 1
    return counts


def render_todo(todo: Mapping[str, str]) -> str:
    """Render a single todo as a terminal-friendly line.

    Args:
        todo: A mapping with ``content`` and (optionally) ``status`` keys.
            A missing ``status`` defaults to ``"pending"``.

    Returns:
        A string such as ``"[x] Write docs"``.

    Raises:
        ValueError: If ``content`` is missing/blank or ``status`` is unknown.

    Examples:
        >>> render_todo({"content": "Write docs"})
        '[ ] Write docs'
    """
    content = str(todo.get("content", "")).strip()
    status = str(todo.get("status", "pending")).lower()
    if not content:
        raise ValueError("todo requires content")
    if status not in _STATUS_MARKERS:
        raise ValueError(f"todo has invalid status {status!r}")
    return f"{_STATUS_MARKERS[status]} {content}"
