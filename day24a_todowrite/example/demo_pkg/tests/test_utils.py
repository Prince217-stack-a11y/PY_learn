"""Tests for :mod:`demo_pkg.utils`.

Run from the ``example`` directory so ``demo_pkg`` is importable::

    cd s05_todo_write/example
    python -m pytest demo_pkg/tests -q
"""

import pytest

import demo_pkg
from demo_pkg.utils import (
    VALID_STATUSES,
    count_by_status,
    render_todo,
    slugify,
)


# -- slugify ---------------------------------------------------------------

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Write Docs!", "write-docs"),
        ("  Hello   World  ", "hello-world"),
        ("already-slugged", "already-slugged"),
        ("A/B\\C", "a-b-c"),
        ("v2.0 Release", "v2-0-release"),
    ],
)
def test_slugify_normalizes_text(text: str, expected: str) -> None:
    assert slugify(text) == expected


@pytest.mark.parametrize("text", ["", "   ", "---", "!!! ..."])
def test_slugify_returns_empty_when_no_alphanumerics(text: str) -> None:
    assert slugify(text) == ""


def test_slugify_lowercases_unicode_letters() -> None:
    assert slugify("École") == "école"


# -- count_by_status -------------------------------------------------------

def test_count_by_status_of_empty_input_is_all_zero() -> None:
    assert count_by_status([]) == {status: 0 for status in VALID_STATUSES}


def test_count_by_status_counts_each_status() -> None:
    todos = [
        {"status": "pending"},
        {"status": "pending"},
        {"status": "in_progress"},
        {"status": "completed"},
        {"status": "completed"},
        {"status": "completed"},
    ]
    assert count_by_status(todos) == {
        "pending": 2,
        "in_progress": 1,
        "completed": 3,
    }


def test_count_by_status_rejects_unknown_status() -> None:
    message = r"todos\[0\] has invalid status 'nope'"
    with pytest.raises(ValueError, match=message):
        count_by_status([{"status": "nope"}])


def test_count_by_status_rejects_missing_status() -> None:
    with pytest.raises(ValueError, match="invalid status None"):
        count_by_status([{"content": "no status here"}])


# -- render_todo -----------------------------------------------------------

@pytest.mark.parametrize(
    ("status", "marker"),
    [("pending", "[ ]"), ("in_progress", "[>]"), ("completed", "[x]")],
)
def test_render_todo_uses_matching_marker(status: str, marker: str) -> None:
    rendered = render_todo({"content": "Ship it", "status": status})
    assert rendered == f"{marker} Ship it"


def test_render_todo_defaults_to_pending_and_strips_content() -> None:
    assert render_todo({"content": "  Ship it  "}) == "[ ] Ship it"


def test_render_todo_is_case_insensitive_for_status() -> None:
    rendered = render_todo({"content": "Ship it", "status": "COMPLETED"})
    assert rendered == "[x] Ship it"


@pytest.mark.parametrize("content", ["", "   "])
def test_render_todo_rejects_blank_content(content: str) -> None:
    with pytest.raises(ValueError, match="todo requires content"):
        render_todo({"content": content})


def test_render_todo_rejects_unknown_status() -> None:
    with pytest.raises(ValueError, match="invalid status 'blocked'"):
        render_todo({"content": "Ship it", "status": "blocked"})


# -- package surface -------------------------------------------------------

def test_package_reexports_public_api() -> None:
    assert demo_pkg.slugify is slugify
    assert demo_pkg.render_todo is render_todo
    assert demo_pkg.count_by_status is count_by_status
    assert demo_pkg.VALID_STATUSES == VALID_STATUSES


def test_package_exposes_version() -> None:
    assert demo_pkg.__version__ == "0.1.0"
