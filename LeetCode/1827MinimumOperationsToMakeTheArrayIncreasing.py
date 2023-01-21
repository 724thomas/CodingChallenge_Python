#https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                ans+=(nums[i]+1-nums[i+1])
                nums[i+1]+=(nums[i]+1-nums[i+1])
        return ans