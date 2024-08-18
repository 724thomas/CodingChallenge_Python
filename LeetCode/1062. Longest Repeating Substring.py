#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        cmax = 0
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    cmax = max(cmax, dp[i][j])

        print(list(s))
        print(list(s))
        print(*dp, sep='\n')
        return cmax