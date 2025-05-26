from typing import Callable

from ._registry import Registry, global_registry
from ._types import TestFunc


def test(_registry: Registry = global_registry) -> Callable[[TestFunc], TestFunc]:
    """Registers a function as a test function to be executed"""

    def decorate(func: TestFunc) -> TestFunc:
        _registry.add(func)
        return func
    return decorate
