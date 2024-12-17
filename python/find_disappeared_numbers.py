# O(n) because iterates through range and time scales with range here
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    output = []
    set_nums = set(nums)
    for x in range(1, len(nums)+1):
        if x not in set_nums:
            output.append(x)
    return output
