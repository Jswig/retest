from ._types import TestFunc


class Registry:
    def __init__(self) -> None:
        self.tests: list[TestFunc] = []

    def add(self, t: TestFunc) -> None:
        self.tests.append(t)

    def get_all(self) -> list[TestFunc] | None:
        return self.tests


global_registry = Registry()
"""Global variable recording all tests registered with retest"""
