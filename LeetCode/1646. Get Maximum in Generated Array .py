# https://leetcode.com/problems/get-maximum-in-generated-array/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        dp={}
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            if i%2==0:
                dp[i]=dp[int(i/2)]
            elif i%2==1:
                dp[i]=dp[i//2]+dp[i//2+1]
        return max(dp.values())