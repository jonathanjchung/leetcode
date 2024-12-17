from python.two_sum import two_sum


def test_two_sum_valid_input():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]


def test_two_sum_with_duplicates():
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]


def test_two_sum_solution_not_at_beginning():
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]
