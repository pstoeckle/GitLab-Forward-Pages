# -*- coding: utf-8 -*-

import pytest
from gl_pages_forward.skeleton import fib

__author__ = "Patrick Stoeckle"
__copyright__ = "Patrick Stoeckle"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
