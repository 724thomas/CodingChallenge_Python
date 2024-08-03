#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append([start, end])
        return stack