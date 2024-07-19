#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, n+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1