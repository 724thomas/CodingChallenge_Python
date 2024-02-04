# https://leetcode.com/problems/meeting-rooms-ii/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        cmax = 0
        for start, end in intervals:
            if not rooms:
                heapq.heappush(rooms, end)
            else:
                while rooms and rooms[0] <= start:
                    heapq.heappop(rooms)
                heapq.heappush(rooms, end)
            cmax = max(cmax, len(rooms))
        return cmax
