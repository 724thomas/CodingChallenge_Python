#

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        ans = 0

        if s and s[0] in "+-":
            if s[0] == "-":
                sign = -1
            s = s[1:]

        for c in s:
            if c in "0123456789":
                ans = ans * 10 + int(c)
            else:
                break

        ans *= sign
        return max(-2**31, min(2**31-1, ans))