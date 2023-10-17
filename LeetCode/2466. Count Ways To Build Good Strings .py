#https://leetcode.com/problems/count-ways-to-build-good-strings/description/

'''
1. 아이디어 :
    backtracking으로 풀면 시간초과가 난다 O(2**n)
    길이에 따라 중복이 절대 없기 떄문에, dp로 memoization을 사용하면 된다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        mod = 10**9 + 7

        def dfs(length):
            if length>high:
                return 0
            if length in dp:
                return dp[length]

            if length>=low:
                dp[length] = 1
            else:
                dp[length] = 0
            dp[length] += dfs(length+zero) + dfs(length+one)
            return dp[length] % mod


        return dfs(0)