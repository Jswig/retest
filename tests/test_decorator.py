import unittest

from retest._decorator import test
from retest._registry import Registry


class TestDecorator(unittest.TestCase):
    def test_decorator_registers_tests(self) -> None:
        registry = Registry()

        @test(_registry=registry)
        def func_1() -> None:
            pass

        @test(_registry=registry)
        def func_2() -> None:
            pass

        result = registry.get_all()
        expected = [
            func_1,
            func_2,
        ]
        self.assertEqual(result, expected)
