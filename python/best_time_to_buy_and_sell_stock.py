# attempt one
# obvious solution is brute forcing, but time limit exceeds
# O(n^2)
def maxProfit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    max_profit = 0
    for left in range(0, len(prices) - 1):
        for right in range(left + 1, len(prices)):
            max_profit = max(max_profit, prices[right] - prices[left])
    return max_profit


# attempt two
# O(N)
def attempt_two(prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r != len(prices):
        if prices[r] < prices[l]:
            l = r
        else:
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
        r += 1
    return max_profit
