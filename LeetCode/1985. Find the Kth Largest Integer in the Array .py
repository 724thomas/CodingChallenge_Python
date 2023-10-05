# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/

'''
1. 아이디어 :
    1. 힙으로 풀 수 있다
    2. 정렬로 풀 수 있다
2. 시간복잡도 :
    1. O(nlogn)
    2. O(nlogn)
3. 자료구조 :
    1. 힙
    2. 배열

'''

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numbers = []
        heapq.heapify(numbers)
        for n in nums:
            heapq.heappush(numbers, -int(n))
        for i in range(k):
            ans = str(-heapq.heappop(numbers))
        return ans

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(sorted([int(x) for x in nums], reverse=True)[k-1])