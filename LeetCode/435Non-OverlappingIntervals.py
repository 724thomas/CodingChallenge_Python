# https://leetcode.com/problems/non-overlapping-intervals/description/

'''
1. 아이디어 :
    1)  정렬을 하고, 각 구간을 비교하여 겹치는 구간 중, 먼저 끝나는 시간을 저장한다.
2. 시간복잡도 :
    1)  O(nlogn) + O(n) = O(nlogn)
    -   정렬 시간 + 탐색 시간
3. 자료구조 :
    1)  List
'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        end = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                end = min(end, intervals[i][1])
                ans+=1
            else:
                end = intervals[i][1]
        return ans