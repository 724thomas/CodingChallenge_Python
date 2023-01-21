#https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        kid=sorted(g)
        cookie=sorted(s)
        kidcount=0
        cookiecount=0
        count=0
        while cookiecount<len(cookie) and kidcount<len(kid):
            if kid[kidcount]<=cookie[cookiecount]:
                kidcount+=1
                cookiecount+=1
                count+=1
            else:
                cookiecount+=1
        return count