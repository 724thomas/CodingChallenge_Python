#https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        for i in range(len(position)):
            position[i]=position[i]%2
        return min(len([x for x in position if x==1]),len([x for x in position if x==0]))