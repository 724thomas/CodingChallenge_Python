# https://leetcode.com/problems/hamming-distance/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = bin(x)[2:]
        x2 = bin(y)[2:]
        print(x1, x2)
        if len(x1) < len(x2):
            x1,x2 = x2, x1
        x2 = "0" * (len(x1)-len(x2)) + x2
        ans = 0
        for i in range(len(x1)):
            if x1[i] != x2[i]:
                ans+=1
        return ans