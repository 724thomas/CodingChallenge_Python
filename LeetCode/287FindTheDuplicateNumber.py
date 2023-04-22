#https://leetcode.com/problems/find-the-duplicate-number/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup=set()
        for num in nums:
            if num not in dup:
                dup.add(num)
            else:
                return num