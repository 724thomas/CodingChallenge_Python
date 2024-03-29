# https://leetcode.com/problems/n-th-tribonacci-number/

'''
1. 아이디어 :
    dp를 사용한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(n-2):
            dp.append(dp[i] + dp[i+1] + dp[i+2])
        return dp[n]