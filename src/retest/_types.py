from typing import Callable

type TestFunc = Callable[[], None]
type TestRunner = Callable[[], bool]
