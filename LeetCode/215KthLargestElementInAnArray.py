# https://leetcode.com/problems/kth-largest-element-in-an-array/

'''
1. 아이디어 :
    1)  정렬하여 출력.
    2)  힙을 사용하여 출력
2. 시간복잡도 :
    1)  O(nlogn)
    2)  O(n) + O(klogn) = O(n)
        -    힙에 n개의 원소를 넣는 시간 + 힙에서 k번 꺼내는 시간
3. 자료구조 :
    1)  배열
    2)   힙
'''



#1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

#2)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums = [-x for x in nums]
        heapq.heapify(negative_nums)
        for i in range(k-1):
            heapq.heappop(negative_nums)
        return -heapq.heappop(negative_nums)