import pytest
from python.contains_duplicate import contains_duplicate


def test_contains_duplicates():
    nums = [1, 2, 3, 1]
    assert contains_duplicate(nums)


def test_contains_no_duplicates():
    nums = [1, 2, 3, 4]
    assert not contains_duplicate(nums)


def test_contains_empty_list():
    nums = []
    assert not contains_duplicate(nums)


def test_contains_one_element():
    nums = [1]
    assert not contains_duplicate(nums)


def test_contains_large_input():
    nums = list(range(10000))
    assert not contains_duplicate(nums)
