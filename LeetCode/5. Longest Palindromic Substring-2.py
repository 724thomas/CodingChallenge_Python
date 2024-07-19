#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(size):
            for i in range(len(s)-size+1):
                ss = s[i:i+size]
                if ss == ss[::-1]:
                    return s[i:i+size]
            return ""

        for i in range(len(s),0,-1):
            val = check(i)
            if val != "":
                return val
