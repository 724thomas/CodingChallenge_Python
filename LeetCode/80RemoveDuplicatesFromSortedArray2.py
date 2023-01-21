# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        total=len(nums)
        count=1
        base=nums[0]
        for i in range(1,len(nums)):
            curr=nums[i]
            if curr==base:
                if count>=2:
                    nums[i]=float('inf')
                    total-=1
                elif count<2:
                    count+=1
            elif curr!=base:
                base=nums[i]
                count=1
        nums.sort()
        print(nums)
        return total
                