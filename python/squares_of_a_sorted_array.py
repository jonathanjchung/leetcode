# attempt one
# cheese solution O(nlog(n))
import collections


def sortedSquares(nums: list[int]) -> list[int]:
    nums = [i ** 2 for i in nums]
    nums.sort()
    return nums


# attempt two
# trying without sort function
# needed to look up solution, had the right idea but wasnt quite there yet
def attempt_two(nums: list[int]) -> list[int]:
    result = collections.deque()
    l, r, = 0, len(nums) - 1
    while l <= r:
        lval, rval = abs(nums[l]), abs(nums[r])
        if lval < rval:
            result.appendleft(rval**2)
            r -= 1
        else:
            result.appendleft(lval**2)
            l += 1
    return list(result)
