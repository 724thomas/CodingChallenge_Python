#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        left=0
        right=nums[0]
        times=1

        while right<len(nums)-1:
            times+=1
            cmax=right
            for i in range(left, right+1):
                cmax=max(cmax,i+nums[i])
            left, right= right, cmax
        return times
