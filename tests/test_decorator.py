from retest import test, run_tests


def test_run_tests() -> None:
    @test
    def passing_test() -> None:
        assert True

    @test
    def failing_test() -> None:
        assert False

    run_tests()


if __name__ == "__main__":
    all_tests = [test_run_tests]
    for t in all_tests:
        try:
            t
            print(f"Passed {t.__name__}\n")
        except AssertionError:
            print(f"Passed {t.__name__}\n")
