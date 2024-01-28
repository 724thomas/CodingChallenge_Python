# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

'''
1. 아이디어 :
    힙 사용
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums = [-x for x in nums]
        heapq.heapify(negative_nums)
        for i in range(k-1):
            heapq.heappop(negative_nums)
        return -heapq.heappop(negative_nums)