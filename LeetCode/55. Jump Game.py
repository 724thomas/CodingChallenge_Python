#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True

        left = 0
        right = nums[0]


        while True:
            cmax = right
            for i in range(left, right+1):
                if i+nums[i] >= len(nums)-1:
                    return True
                cmax = max(cmax, i + nums[i])
            if right == cmax:
                return False
            left, right = right, cmax
