#https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

'''
1. 아이디어 :
    1) 힙으로 풀 수 있다.
    2) 이진탐색으로 구할 수 있다
2. 시간복잡도 :
    1) init = O(n) , add = 2 * O(logn)
    2) init, add = 배열에 추가하고 정렬-O(n) / 이진탐색으로 하나씩 추가-O(logn)
3. 자료구조 :
    1) 힙
    2) 배열
'''

# 2)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.minHeap)>k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)> self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 1)
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numList = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        start = 0
        end = len(self.numList)-1
        def binary_search(numList, value):
            start = 0
            end = len(numList)
            while start<=end:
                mid = (start+end)//2
                if mid >= len(numList):
                    return len(numList)
                if self.numList[mid] == value:
                    return mid
                elif self.numList[mid] < value:
                    start = mid + 1
                elif self.numList[mid] > value:
                    end = mid - 1
            return start
        index = binary_search(self.numList,val)
        self.numList.insert(index, val)
        return self.numList[len(self.numList)-self.k]
'''