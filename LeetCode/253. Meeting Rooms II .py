# https://leetcode.com/problems/meeting-rooms-ii/description/

'''
1. 아이디어 :
    시작시간, 끝나는 시간을 배열에 정렬하여 넣는다.
    투포인터로, 시작시간이 끝나는 시간보다 작으면 방배정이 하나 되고 포인터를 옮기고,
    반대면 방을 하나 빼고 포인터를 옮긴다.
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    배열
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = sorted([time[0] for time in intervals])
        end = sorted([time[1] for time in intervals])

        start_pointer = 0
        end_pointer = 0
        count = 0
        cmax = 0

        while start_pointer<len(intervals):
            if start[start_pointer] < end[end_pointer]:
                count+=1
                start_pointer+=1
            else:
                count-=1
                end_pointer+=1
            cmax = max(cmax, count)

        return cmax



