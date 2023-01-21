#https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        alist=[]
        for i in range(n+1):
            alist.append(bin(i)[2:].count("1"))
        return (alist)
        