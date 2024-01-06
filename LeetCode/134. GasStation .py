#https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tt,ct,cp=0,0,0
        for i in range(len(gas)):
            tt+=gas[i]-cost[i]
            if ct+gas[i]-cost[i]>=0:
                ct+=gas[i]-cost[i]
            else:
                ct=0
                cp=i+1
        return cp if tt>=0 else -1
                