#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place=0
        for i in range(len(nums)):
            if nums[i]!=nums[place]:
                place+=1
                nums[place]=nums[i]

        print(nums)
        return place+1
