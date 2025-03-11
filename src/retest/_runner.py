from ._decorator import get_registered_tests

def run_tests() -> None:
    registered_tests = get_registered_tests()
    if registered_tests is not None:
        for test in registered_tests:
            test()
