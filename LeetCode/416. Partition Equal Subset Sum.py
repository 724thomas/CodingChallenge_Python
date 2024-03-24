#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        target = total//2
        memo = {}

        def bt(idx, left, right):
            if left>target or right>target:
                return False
            if idx == len(nums):
                return left==right
            if (idx, left, right) in memo:
                return memo[(idx,left,right)]

            check = bt(idx+1, left+nums[idx], right) or bt(idx+1, left, right+nums[idx])
            memo[(idx, left, right)] = check
            return memo[(idx, left, right)]

        return bt(0,0,0)


