#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        res = max(nums)

        curr_min, curr_max = 1, 1

        for i in range(n):
            tmp = curr_max
            curr_max = max(nums[i] * curr_min, nums[i] * curr_max, nums[i])
            curr_min = min(nums[i] * curr_min, nums[i] * tmp, nums[i])
            res = max(res, curr_max)

        return res