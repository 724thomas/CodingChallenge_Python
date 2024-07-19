#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp)