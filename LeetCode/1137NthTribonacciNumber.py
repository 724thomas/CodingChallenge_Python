#https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:

        alist={}
        alist[0]=0
        alist[1]=1
        alist[2]=1
        for i in range(3,n+1):
            alist[i]=alist[i-3]+alist[i-2]+alist[i-1]
        return alist[n]