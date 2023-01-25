#https://leetcode.com/problems/kth-largest-element-in-an-array/description/

'''
1. 아이디어 :
    1)  heapq를 사용할 수 있다
    2)  배열을 정렬할 수 있다.
2. 시간복잡도 :
    1)  O(n) + O(k log n) = O(n log k)
    2)  O(n) = O(nlogn)
    * 이론상 최악의 경우, 1)번이 더 빠르지만, 실제로는 2)번이 더 빠르다
3. 자료구조 :
    1)  heapq
    2)  배열
'''

#1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = []
        for num in nums:
            ans.append([-num,num])
        heapq.heapify(ans)
        for i in range(k-1):
            heapq.heappop(ans)
        return ans[0][1]

#2)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return sorted(nums, reverse=True)[k-1]