#https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def minimumMoves(self, s: str) -> int:
        count=0
        while len(s)>=3:
            if s[0]=="O":
                s=s[1:]
            elif s[0]=="X" or s[1]=="X" or s[2]=="X":
                count+=1
                s=s[3:]
        if "X" in s:
            count+=1
        return count