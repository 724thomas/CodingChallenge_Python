#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        ans=[""]*len(s)
        for w in s:
            ans[int(w[-1])-1]=w[:-1]
        return " ".join(ans)