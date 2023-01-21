#https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer=0
        for char in s:
            while True:
                try:
                    if char == t[pointer]:
                        pointer+=1
                        break
                    elif char!=t[pointer]:
                        pointer+=1
                except:
                    return False
        return True
