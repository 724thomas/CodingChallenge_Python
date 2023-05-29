# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

'''
1. 아이디어 :
    최소힙을 사용하여 -pile을 저장하고, k번 만큼 반복문을 돌면서 가장 큰 pile을 꺼내서 절반으로 나눈 뒤 다시 최소힙에 넣는다.
2. 시간복잡도 :
    O(NlogN)
3. 자료구조 :
    힙
'''

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for pile in piles:
            heapq.heappush(max_heap, -pile)
        for _ in range(k):
            pile = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(pile - (pile//2)))
        return -sum(max_heap)
