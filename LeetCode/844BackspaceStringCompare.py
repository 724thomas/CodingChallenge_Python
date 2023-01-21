#https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def delsha(s):
            while "#" in s:
                idx=s.index("#")
                if idx!=0:
                    s=s[:idx-1]+s[idx+1:]
                else:
                    s=s[1:]
                print(s)
            return s

        s=delsha(s)
        t=delsha(t)
        return s==t