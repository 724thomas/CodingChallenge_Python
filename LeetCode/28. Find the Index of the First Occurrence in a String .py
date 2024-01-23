# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle,0) if needle in haystack else -1