from python.missing_number import missing_number


def test_missing_unordered():
    nums = [3, 0, 1]
    assert missing_number(nums) == 2


def test_missing_ordered():
    nums = [0, 1, 2, 3, 5]
    assert missing_number(nums) == 4


def test_missing_number_greater_than_range():
    nums = [0, 1]
    assert missing_number(nums) == 2


def test_empty_list():
    nums = []
    assert missing_number(nums) == 0


def test_missing_zero():
    nums = [1, 2, 3]
    assert missing_number(nums) == 0
