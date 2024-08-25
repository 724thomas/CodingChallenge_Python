#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque, defaultdict
import heapq
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dir = [-1, 0, 1]

        prev = defaultdict(int)
        prev[(0,0,m-1)] = grid[0][0] + grid[0][m-1] #row, r1, r2
        for i in range(n-1):
            curr = defaultdict(int)

            for k, total in prev.items():
                row, r1, r2 = k
                for y1 in dir:
                    for y2 in dir:
                        ny1, ny2 = r1+y1, r2+y2
                        if not (0<=ny1<m and 0<=ny2<m): continue
                        new_total = total + grid[row+1][ny1] if ny1 == ny2 else total + grid[row+1][ny1] + grid[row+1][ny2]
                        curr[(row+1, ny1, ny2)] = max(curr[(row+1, ny1, ny2)], new_total)

            prev = curr
        return max(prev.values())
