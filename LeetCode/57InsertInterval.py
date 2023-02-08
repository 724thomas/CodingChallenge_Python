# https://leetcode.com/problems/insert-interval/description/

'''
1. 아이디어 :
    1)  newInterval을 추가 한후, sorting을 하고, 각 구간을 비교하여 겹치는 구간을 합친다.
2. 시간복잡도 :
    1)  O(nlogn) + O(n) = O(nlogn)
    -   정렬 시간 + 탐색 시간
3. 자료구조 :
    1)  'List
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            if intervals[i][0]<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans;