#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        def get_next_cords(x, y):
            cords = []
            for x2, y2 in dir:
                nx, ny = x+x2, y+y2
                while 0<=nx<n and 0<=ny<m and maze[nx][ny] == 0:
                    nx += x2
                    ny += y2
                if not(nx-x2 == x and ny-y2 == y):
                    cords.append((nx-x2, ny-y2))
            return cords

        min_heap = [[0, start[0], start[1]]]
        visited = set()

        while min_heap:
            curr, x, y = heapq.heappop(min_heap)
            if x == destination[0] and y == destination[1]:
                return curr

            if (x,y) in visited:
                continue
            visited.add((x,y))

            for x2, y2 in get_next_cords(x, y):
                heapq.heappush(min_heap, (curr + abs(x-x2) + abs(y-y2), x2, y2))

        return -1
