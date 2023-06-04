# https://leetcode.com/problems/unique-paths-iii/description/

'''
1. 아이디어 :
    1) 시작점과 방문하지 말아야할 점을 찾는다.
    2) dfs를 사용하여 조건에 x,y가 0보다 작거나, len보다 크거나, 방문을 했으면 리턴
    3) 모든곳을 방문하고 도착지가 2이면 카운트 하나 추가
    4) 4방향으로 dfs를 수행한다.
2. 시간복잡도 :
    O(N*M) + O(4^(N*M))
    시작점과 visited 추가 + dfs
3. 자료구조 :
    해시셋, 리스트
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        total = len(grid) * len(grid[0])-1
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    visited.add((i,j))
                if grid[i][j] == 1:
                    start = (i,j)

        dir = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(row,col):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or (row,col) in visited:
                return

            if len(visited) == total and grid[row][col]==2:
                self.count+=1

            for d in dir:
                dx, dy = d
                visited.add((row, col))
                dfs(row+dx, col+dy)
                visited.remove((row, col))

        dfs(start[0],start[1])
        return self.count
