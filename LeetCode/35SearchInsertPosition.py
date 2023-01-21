#https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            pointer=0
            while pointer<len(nums) and nums[pointer]<target:
                pointer+=1
            return pointer
