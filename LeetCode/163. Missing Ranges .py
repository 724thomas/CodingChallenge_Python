# https://leetcode.com/problems/missing-ranges/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums = nums + [upper + 1]
        ans = []

        for n in nums:
            if lower < n:
                ans.append([lower, n - 1])
            lower = n + 1
        return ans
