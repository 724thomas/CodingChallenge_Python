# https://leetcode.com/problems/min-cost-climbing-stairs/description/

'''
1. 아이디어 :
    dp를 사용하여, 각 계단을 밟는데 드는 최소 비용을 구한다.
2. 시간복잡도 :
    O(n) : n은 cost의 길이
3. 자료구조 :
    리스트
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])