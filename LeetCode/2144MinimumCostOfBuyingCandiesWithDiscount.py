#https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans=0
        cost=sorted(cost)[::-1]
        for i in range(len(cost)):
            if i%3!=2:
                ans+=cost[i]
        return ans
