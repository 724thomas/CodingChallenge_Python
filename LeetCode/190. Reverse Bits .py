# https://leetcode.com/problems/reverse-bits/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:]
        m=[0] * len(n)
        for i in range(len(n)):
            m[-1-i] = n[i]
        m = "".join(m) + "0" * (32-len(n))
        return (int(m,2))

