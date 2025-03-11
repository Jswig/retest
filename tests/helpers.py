"""Helpers for boostrapping testing"""
import sys
from typing import Callable

def execute_test_cases(tests: list[Callable]):
    tests_passed = []
    for t in tests:
        try:
            t()
            print(f"Passed {t.__name__}")
            tests_passed.append(True)
        except AssertionError:
            print(f"Failed {t.__name__}")
            tests_passed.append(False)
    if all(tests_passed):
        sys.exit(0)
    else:
        sys.exit(1)
