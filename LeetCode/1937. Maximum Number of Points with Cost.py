#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        for row in range(1, n):
            left = [points[row-1][0]]
            right = [points[row-1][-1]]
            for prev in range(1, m):
                left.append(max(left[-1]-1, points[row-1][prev]))
                right.append(max(right[-1]-1, points[row-1][-1-prev]))
            for col in range(m):
                points[row][col] += max(left[col], right[-1-col])

        return max(points[-1])
