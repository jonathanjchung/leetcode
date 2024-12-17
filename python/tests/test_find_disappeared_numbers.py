from python.find_disappeared_numbers import find_disappeared_numbers


def test_missing_numbers():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    assert find_disappeared_numbers(nums) == [5, 6]


def test_no_missing_numbers():
    nums = [1, 2, 3, 4, 5]
    assert find_disappeared_numbers(nums) == []


def test_empty_input():
    nums = []
    assert find_disappeared_numbers(nums) == []


def test_many_numbers_missing():
    nums = [7, 7, 7, 7, 7, 7, 7]
    assert find_disappeared_numbers(nums) == [1, 2, 3, 4, 5, 6]


def test_contains_dupes():
    nums = [1, 1, 2, 2]
    assert find_disappeared_numbers(nums) == [3, 4]
