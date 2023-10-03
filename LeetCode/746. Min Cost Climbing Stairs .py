# https://leetcode.com/problems/min-cost-climbing-stairs/description/

'''
1. 아이디어 :
    Dp로 풀 수 있다.
    costs = [0,0]으로 시작하고, i=2, len(cost)+1까지 for문을 도는데,
    costs[i-2]+cost[i-2], costs[i-1]+cost[i-1] 중 작은 값을 넣는다.
    costs[-1]을 리턴
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0,0]
        for i in range(2, len(cost)+1):
            costs.append(min(costs[i-2]+cost[i-2], costs[i-1]+cost[i-1]))
        return costs[-1]