def two_sum(nums: list[int], target: int) -> list[int]:
    seen_nums = dict()
    for index, val in enumerate(nums):
        lookingFor = target - val
        if lookingFor in seen_nums:
            return [seen_nums.get(lookingFor), index]
        seen_nums[val] = index
    return []
