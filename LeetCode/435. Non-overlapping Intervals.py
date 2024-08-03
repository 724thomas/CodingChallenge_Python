#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start < prev:
                count+=1
                prev = min(prev, end)
            else:
                prev = end
        return count