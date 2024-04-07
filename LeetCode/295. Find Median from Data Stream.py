#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        #left에 일단 밀어넣는다.
        heapq.heappush(self.left, -num)

        #left, right 둘다 값이 존재하고, left에서 제일 큰 값 > right에서 제일 작은값
        if (self.left and self.right and ( -self.left[0]) > self.right[0]):
            popped = -heapq.heappop(self.left)
            heapq.heappush(self.right, popped)

        #left의 길이가 right+1 보다 크면,
        if len(self.left) > len(self.right) + 1:
            popped = -heapq.heappop(self.left)
            heapq.heappush(self.right, popped)

        #left+1의 길이가 right 보다 작으면,
        if len(self.left) + 1 < len(self.right):
            popped = -heapq.heappop(self.right)
            heapq.heappush(self.left, popped)


    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]

        return (-1 * self.left[0] + self.right[0])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()