Design goals
============

``retest`` aims to have less boilerplate that ``unittest``, less magic than ``pytest``,
and more features than both.


Explicit
--------

Reading a ``retest`` file does not require special knowledge of the framework's
execution model. ``retest`` features are always accessed through explicit imports.
``retest`` picks readability over conciseness when there is a trade-off between the two.

Concise
-------

Writing a test should be almost as simple as defining a Python function.
``retest`` aims to be competitive with ``pytest`` in eliminating boilerplate from 
test definition.


REPL-friendly
-------------

``retest`` test functions are "just functions". They are easy to author and run
in an IPython session. REPL-driven development is one of Python's greatest
strengths, so executing tests should be easy in any context without requiring going
through a specialized CLI.

Orthorgonal
-----------

Features do not overlap. Users do not have to choose which feature to employ, it should
always be obvious what is the correct one. ``retest`` leans on the standard library
as much as possible.

Self-contained
--------------

``retest`` uses as few external dependencies as possible so as to keep test environment
setup simple. Moreover, ``retest`` aims to be "batteries included", such that no
additonal top-level testing dependencies are needed in common testing scenarios.
``retest`` will include built-in support for:

- ``async`` test function execution
- benchmarks
- parallel execution of tests
- setup and teardown of test dependencies

Composable
----------

``retest`` should be easy to compose with other testing tools without requiring
explicit support for ``retest`` via e.g. plugins.
