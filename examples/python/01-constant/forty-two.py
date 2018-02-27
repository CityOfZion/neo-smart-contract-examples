"""
License: MIT
Author: Travis Lin
Version: 1
Contract Hash: 7eda0d8656310d97d6b342cd831f8d1be7186ee8
Date Created: 2018-02-27
Date Modified: 2018-02-27
Example Build Test Command: `build ./examples/python/01-constant/forty-two.py test ff 02 False False`
Example Import Command: `import contract ./examples/python/01-constant/forty-two.py ff 02 False False`
Example Invoke: `testinvoke 7eda0d8656310d97d6b342cd831f8d1be7186ee8`
"""


def Main():
    """
    :return: Static number value.
    :rtype: int
    """
    return 42  # Direct return an integer without usage of local variable
