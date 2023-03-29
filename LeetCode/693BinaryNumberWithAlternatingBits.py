#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=bin(n)[2:]
        return not("11" in n or "00" in n)