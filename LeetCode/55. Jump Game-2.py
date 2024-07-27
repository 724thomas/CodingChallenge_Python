#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cmax = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= cmax:
                cmax = i
        return cmax == 0