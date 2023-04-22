#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs=[]
        cmax=-float("inf")
        for i in range(len(nums)//2):
            cmax=max(cmax,(nums[i]+nums[-i-1]))

        return cmax