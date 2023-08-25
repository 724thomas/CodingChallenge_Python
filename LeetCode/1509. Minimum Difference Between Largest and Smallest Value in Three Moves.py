#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0

        nums.sort()
        diff=len(nums)-4
        cmin=float("inf")
        for i in range(len(nums)-diff):
            cmin=min(cmin,nums[i+diff]-nums[i])
        return cmin