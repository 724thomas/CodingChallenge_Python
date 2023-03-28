#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def shortestDistance(self, w: List[str], word1: str, word2: str) -> int:
        w1=[]
        w2=[]
        for i in range(len(w)):
            if w[i]==word1:
                w1.append(i)
            elif w[i]==word2:
                w2.append(i)
        print(w1,w2)
        cmin=float('inf')
        for n1 in w1:
            for n2 in w2:
                cmin=min(cmin,abs(n1-n2))
        return cmin