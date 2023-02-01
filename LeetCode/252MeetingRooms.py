# https://leetcode.com/problems/meeting-rooms/description/

'''
1. 아이디어 :
    1)  시작 시간 기준으로 정렬하고, 시작 시간이 이전 종료 시간보다 작으면 False를 반환한다.
2. 시간복잡도 :
    1)  O(nlogn) + O(n) = O(nlogn)
    -   정렬 시간 + 탐색 시간
3. 자료구조 :
    1)  List
'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)-1):
            if intervals[i+1][0]<intervals[i][1]:
                return False
        return True