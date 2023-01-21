#https://leetcode.com/problems/two-sum-less-than-k/

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        max=0
        left=0
        right=len(nums)-1
        while left<right:
            temp=nums[left]+nums[right]
            if temp>=k:
                right-=1
            else:
                if temp>max:
                    max=temp
                left+=1
        return max if max!=0 else -1