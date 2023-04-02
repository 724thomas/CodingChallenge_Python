#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s=s1+" "+s2
        c=Counter(s.split(" "))

        return [w for w in c if c[w]==1]
