#https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        i=0
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=-nums[i]
                k-=1
                if k==0:
                    return sum(nums)

        if k%2==0:
            return sum(nums)
        else:
            nums=sorted(nums)
            return sum(nums[1::])-nums[0]
