import functools

from ._types import TestFunc, TestRunner

_registered_tests: list[TestRunner] | None = None


def test(func: TestFunc) -> TestRunner:
    """Registers a function as a test function to be executed by retest"""

    @functools.wraps(func)
    def run_test() -> bool:
        try:
            func()
            return True
        except AssertionError:
            return False

    global _registered_tests
    if _registered_tests is None:
        _registered_tests = []
    _registered_tests.append(run_test)
    return run_test


def get_registered_tests() -> list[TestRunner] | None:
    return _registered_tests
