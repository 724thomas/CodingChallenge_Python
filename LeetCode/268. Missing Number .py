# https://leetcode.com/problems/missing-number/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(n)
3. 자료구조 :

'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return ((len(nums)*(len(nums)+1))//2) - sum(nums)