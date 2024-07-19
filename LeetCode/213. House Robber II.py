#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size <=2:
            return max(nums)
        ans = 0
        dp = [[0,0] for _ in range(size)]
        for i in range(size-1):
            dp[i][0] = nums[i] + max(dp[i-2][0],dp[i-3][0])
            dp[i+1][1] = nums[i+1] + max(dp[i-1][1],dp[i-2][1])
            ans = max(ans, dp[i][0], dp[i+1][1])
        return ans