# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

'''
1. 아이디어 :
    needle이 haystack에 있는지 확인하고, 있다면 index를 반환하고, 없다면 -1을 반환한다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    배열
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle,0) if needle in haystack else -1