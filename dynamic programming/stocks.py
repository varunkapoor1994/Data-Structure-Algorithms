"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0
    if len(prices) == 1:
        return 0
    max_profit = 0
    cp = prices[0]
    for price in prices:
        max_profit = max(price - cp, max_profit)
        cp = min(cp, price)
    return max_profit
