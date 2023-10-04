# https://leetcode.com/problems/seat-reservation-manager/description/

'''
1. 아이디어 :
    heapq로 구현
2. 시간복잡도 :
    O(logn)
3. 자료구조 :
    힙
'''

import heapq
class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1,n+1)]
        heapq.heapify(self.seats)
    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)