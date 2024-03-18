#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[0]+nums[2])

        dp = [nums[0], nums[1], nums[0]+nums[2]]
        for i in range(3, len(nums)):
            cmax = nums[i] + max(
                dp[i-2], dp[i-3]
            )
            dp.append(cmax)
        return max(dp)
