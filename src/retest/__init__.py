__version__ = "0.1.0"

from ._decorator import test
from ._runner import run_tests
from ._types import TestFunc, TestRunner

__all__ = [
    "test",
    "run_tests",
    "TestFunc",
    "TestRunner",
]
