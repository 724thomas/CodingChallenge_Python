#https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums)[::-1]
        for i in range(0,len(nums)-2):
            if nums[i+2]+nums[i+1]>nums[i]:
                return nums[i+2]+nums[i+1]+nums[i]
        return 0
                