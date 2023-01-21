#https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):
            if n<=1:
                return 0
            if n in hm:
                return hm[n]
            one_down = dp(n-1)+cost[n-1]
            two_down = dp(n-2)+cost[n-2]
            temp=min(one_down,two_down)
            hm[n]=temp
            return temp

        hm={}
        return dp(len(cost))
