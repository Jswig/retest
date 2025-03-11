import functools
from typing import Callable, Union


type TestFunc = Callable[[], None]
type TestRunner = Callable[[], bool]

_registered_tests: Union[list[TestRunner], None] = None


def test(func: TestFunc) -> TestRunner:
    """Decorator to define a test case to be executed by retest"""

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


def run_tests() -> None:
    global _registered_tests
    if _registered_tests is not None:
        for test in _registered_tests:
            test()
