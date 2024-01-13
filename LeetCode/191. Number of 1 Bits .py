# https://leetcode.com/problems/number-of-1-bits/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
