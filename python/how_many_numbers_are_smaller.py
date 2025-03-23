# first attempt O(n^2)
def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    results = []
    for i, v in enumerate(nums):
        count = 0
        for val in nums:
            if v > val:
                count += 1
        results.append(count)
    return results


# second attempt, think two sum, i think O(nlogn)
def attempt_two(nums: list[int]) -> list[int]:
    temp = sorted(nums)
    d = dict()
    for i, v in enumerate(temp):
        if v not in d:
            d[v] = i
    results = []
    for i in nums:
        results.append(d[i])
    return results
