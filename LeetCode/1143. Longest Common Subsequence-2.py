#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def longestCommonSubsequence(self, X: str, Y: str) -> int:
        def lcs(s1, s2):
            n = len(s1)
            m = len(s2)
            dp = [[0] * (m + 1) for _ in range(n + 1)]

            for i in range(n + 1):
                for j in range(m + 1):
                    if i == 0 or j == 0:
                        dp[i][j] = 0
                    elif s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            return dp[n][m]

        return lcs(X, Y)