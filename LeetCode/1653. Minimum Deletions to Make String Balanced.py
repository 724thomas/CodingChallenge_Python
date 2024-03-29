#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def minimumDeletions(self, s: str) -> int:
        Acounts = []
        Bcounts = []

        As=Bs = 0
        for i in range(len(s)):
            Acounts.append(As)
            Bcounts.append(Bs)
            As += s[i] == 'b'
            Bs += s[-1-i] == "a"

        return min([Acounts[i]+Bcounts[-1-i] for i in range(len(s))])
