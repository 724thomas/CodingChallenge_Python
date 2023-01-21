#https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict={}
        news=""
        for i in s:
            if i not in sdict:
                sdict[i]=len(sdict)
            news+=str(sdict[i])+"."
        print(news)
        sdict={}
        newt=""
        for i in t:
            if i not in sdict:
                sdict[i]=len(sdict)
            newt+=str(sdict[i])+"."
        print(newt)
        return newt==news
