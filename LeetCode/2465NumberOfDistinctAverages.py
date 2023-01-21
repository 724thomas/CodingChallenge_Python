#https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        l=0
        r=len(nums)-1
        alist=[]
        while l<r:
            if nums[l]+nums[r] not in alist:
                alist.append(nums[l]+nums[r])
            l+=1
            r-=1
        return len(alist)