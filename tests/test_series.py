from series import __version__
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_one_returns_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two_returns_one():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_neg_1_return_invalid():
    actual = fibonacci(-1)
    expected = 'Invalid input'
    assert actual == expected

def test_fibonacci_str_return_invalid():
    actual = fibonacci("A")
    expected = 'Invalid input'
    assert actual == expected

def test_lucas_zero_returns_two():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one_returns_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_four_returns_seven():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_neg_one_returns_invalid():
    actual = lucas(-1)
    expected = "Invalid input"
    assert actual == expected

def test_sum_series_three_only_returns_two():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_series_three_two_one_returns_two():
    actual = sum_series(3,2,1)
    expected = 4
    assert actual == expected

def test_sum_series_three_four_six_returns_sixteen():
    actual = sum_series(3,4,6)
    expected = 16
    assert actual == expected
