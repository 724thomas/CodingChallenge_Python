#https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        max=int(len(s)/2);
        if len(s)%2==1:
            return False
        for i in range(max):
            s=s.replace("[]","")
            s=s.replace("()","")
            s=s.replace("{}","")
        if s=="":
            return True
        return False
