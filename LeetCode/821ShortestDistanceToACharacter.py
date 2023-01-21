#https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ml=-len(s)
        idx=0
        alist=[]
        for i in range(len(s)):
            if s[i]!=c:
                alist.append(i-ml)
            else:
                alist.append(0)
                ml=i
        ml=len(s)*2
        
        for i in range(len(s)-1,-1,-1):
            if s[i]!=c:
                alist[i]=min(ml-i,alist[i])
            else:
                ml=i

        return alist