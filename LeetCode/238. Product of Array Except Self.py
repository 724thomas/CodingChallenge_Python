#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        n = len(nums)
        if zeros >=2:
            return [0] * n

        ans = [0] * n
        left, right = [1] * (n+1), [1] * (n+1)

        for i in range(n-1):
            left[i] = left[i-1] * nums[i]
            right[n-1-i] = right[n-i] * nums[n-1-i]

        return [right[1]] + [left[i-1] * right[i+1] for i in range(1, n-1)] + [left[-3]]
