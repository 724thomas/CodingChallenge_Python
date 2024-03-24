#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dir = ((0,1), (0,-1), (-1,0), (1,0))
        visited=set()
        queue = deque()
        left = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    left +=1
        if not queue:
            return 0 if not left else -1
        count = -1
        visited=set()
        while True:

            if not queue:
                if len(visited) != left:
                    return-1
                return count
            count+=1
            new_queue = deque()
            while queue:
                row, col = queue.popleft()
                grid[row][col] = 2
                for row2, col2 in dir:
                    nrow = row+row2
                    ncol = col+col2
                    if 0<=nrow<len(grid) and 0<=ncol<len(grid[0]) and grid[nrow][ncol] == 1 and (nrow, ncol) not in visited:
                        visited.add((nrow,ncol))
                        new_queue.append([nrow, ncol])
            queue = new_queue

