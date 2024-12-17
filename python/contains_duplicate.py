def contains_duplicate(nums: list) -> bool:
    count = dict()
    for x in nums:
        count[x] = count.get(x, 0) + 1
    for key in count:
        if count[key] > 1:
            return True
    return False
