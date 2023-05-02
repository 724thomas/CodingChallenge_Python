#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        cmax=[-1,-1]
        cmin=[float("inf"),-1]
        for i in range(len(nums)):
            if nums[i]>=cmax[0]:
                cmax=[nums[i],i]
            if nums[i]<cmin[0]:
                cmin=[nums[i],i]

        ans=len(nums)-cmax[1]+cmin[1]-1
        if cmax[1]>cmin[1]:
            return ans
        else:
            return ans-1