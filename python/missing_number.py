# O(nlogn): sorted has O(nlogn) which slows down solution, would've been linear O(n) from for loop
# def missing_number(nums: list[int]) -> int:
#     ordered = sorted(nums)
#     curr = 0
#     for val in ordered:
#         if curr != val:
#             return curr
#         curr += 1
#     return curr


# O(n): iterates through sum twice, where sum is O(n) and range/len are O(1)
def missing_number(nums: list[int]) -> int:
    return sum(range(len(nums)+1)) - sum(nums)
