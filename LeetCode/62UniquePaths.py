#https://leetcode.com/problems/unique-paths/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[1] * n for x in range(m)]
        for c in range(1, n):
            for r in range(1, m):
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]
