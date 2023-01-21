#https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==k:
            return max(nums)-min(nums)
        nums.sort()
        print(nums)
        lp=0
        rp=lp+k-1
        tmin=nums[-1]
        while rp<len(nums):
            cmin=nums[rp]-nums[lp]
            if cmin<tmin:
                tmin=cmin
            lp+=1
            rp+=1
        return tmin