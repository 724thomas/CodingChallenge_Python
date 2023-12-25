# https://leetcode.com/problems/the-maze/description/

'''
1. 아이디어 :
    bfs로 갈 수 있는 곳까지 이동시킨다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    큐
'''

from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        dir = [1,0],[-1,0],[0,1],[0,-1]

        visited = set()
        queue = deque()
        queue.append(start)

        while queue:
            row1, col1 = queue.popleft()

            if row1 == destination[0] and col1 == destination[1]:
                return True

            for row2, col2 in dir:
                nrow = row1+row2
                ncol = col1+col2

                while 0<=nrow<len(maze) and 0<=ncol<len(maze[0]) and maze[nrow][ncol] == 0:
                    nrow+=row2
                    ncol+=col2

                nrow-=row2
                ncol-=col2

                if (nrow,ncol) not in visited:
                    queue.append((nrow,ncol))
                    visited.add((nrow, ncol))

        return False