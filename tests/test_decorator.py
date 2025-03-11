from retest._decorator import test, get_registered_tests

from helpers import execute_test_cases

def run_defined_test_passing() -> None:
    @test
    def assert_no_error() -> None:
        assert 1 == 1

    result = assert_no_error()
    expected = True
    assert result == expected


def run_defined_test_failing() -> None:
    @test
    def assert_raise_error() -> None:
        assert 1 == 0  # type: ignore

    result = assert_raise_error()
    expected = False
    assert result == expected


def get_registered_tests_returns_all_defined_tests() -> None:
    @test
    def func_1() -> None:
        pass

    @test
    def func_2() -> None:
        pass

    result = get_registered_tests()
    expected = [
        func_1,
        func_2,
    ]
    assert result == expected


if __name__ == "__main__":
    all_tests = [
        get_registered_tests_returns_all_defined_tests,
        run_defined_test_passing,
        run_defined_test_failing,
    ]
    execute_test_cases(all_tests)