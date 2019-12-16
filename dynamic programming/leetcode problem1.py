"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping
you from robbingeach of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house,determine the maximum amount of money you can rob without alerting
the police.
"""


def rob(nums: List[int]):
    max_including = nums[0]
    max_excluding = 0
    for num in nums[1:]:
        temp = max_excluding + num
        max_excluding = max(max_including, max_excluding)
        max_including = temp
    return max(max_including, max_excluding)
