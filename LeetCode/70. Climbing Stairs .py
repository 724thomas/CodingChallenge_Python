# https://leetcode.com/problems/climbing-stairs/description/

'''
1. 아이디어 :
    dp의 전형적인 문제
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        if n <=2:
            return dp[n]

        for i in range(3, n+1):
            dp.append( dp[i-2] + dp[i-1])
        return dp[-1]