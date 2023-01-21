#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt,cntR,cntL=0,0,0
        for letter in s:
            if letter == "R":
                cntR+=1
            elif letter == "L":
                cntL+=1
            if cntR==cntL:
                cnt+=1
                cntR=0
                cntL=0
        return cnt
        