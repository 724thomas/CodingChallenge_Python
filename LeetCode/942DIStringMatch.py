#https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        min=0
        max=len(s)
        alist=[]
        for i in s:
            if i=="D":
                alist.append(max)
                max-=1
            else:
                alist.append(min)
                min+=1
        alist.append(min)
        return alist