#https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lp=0
        ans=[0 for x in range(len(nums))]
        for i in nums:
            if i != 0:
                ans[lp]=i
                lp+=1
        for i in range(len(ans)):
            nums[i]=ans[i]



