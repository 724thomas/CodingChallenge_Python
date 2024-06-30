#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.left = [] #제일 큰 값부터
        self.right = [] #제일 작은 값부터

    def addNum(self, num: int) -> None:
        #왼쪽 길이가 항상 오른쪽 길이보다 같거나 1 더 많아야한다.
        heappush(self.left, -num)

        #왼쪽 값들은 항상 오른쪽 값들보다 작아야함.
        #만약 숫자를 삽입했는데 기존 왼쪽값[0]보다 더 크면, 중앙값이 될 수 없으므로, 오른쪽에 넣는다.
        if self.left and self.right:
            if -self.left[0] > self.right[0]:
                heappush(self.right, -heappop(self.left))

        #왼쪽 길이가 오른쪽보다 2이상 크면 벨런스를 맞춰준다. [x,x,x] , [y] -> [x,x] , [y,y]
        if len(self.left) >= len(self.right) + 2:
            heappush(self.right, -heappop(self.left))

        #오른쪽 길이가 더 길지 않도록 맞춰준다 [x,x] , [y,y,y] -> [x,x,x] , [y, y]
        if len(self.right) > len(self.left):
            heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        if (len(self.right) + len(self.left)) % 2 == 1:
            return -self.left[0]
        return (-self.left[0] + self.right[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()