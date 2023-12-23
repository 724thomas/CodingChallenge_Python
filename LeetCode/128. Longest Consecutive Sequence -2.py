#https://leetcode.com/problems/longest-consecutive-sequence/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        cmax = 0

        for n in nums:
            if n not in visited:
                visited.add(n)
                curr_length = 1
                while n+curr_length in nums:
                    visited.add(n+curr_length)
                    curr_length += 1
                cmax = max(cmax, curr_length)

        return cmax

