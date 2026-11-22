"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import logshape


def test_version_is_set() -> None:
    assert logshape.__version__
