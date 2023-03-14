# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

'''
1. 아이디어 :
    Pacific과 Atlantic 둘다 만족하려는 dfs를 만들기보다, pacific을 만족하는 dfs, atlantic을 만족하는 dfs를 따로 만들고,
    합집합을 만들면 된다.
2. 시간복잡도 :
    O(2mn)
3. 자료구조 :
    해시셋
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        pac = set()
        atl = set()
        visited = set()

        def dfs(x,y, prev, PorA):
            if x<0 or y<0 or x==row or y==col or (x,y) in visited or prev > heights[x][y]:
                return

            if PorA == "P":
                if (x,y) in pac:
                    return
                pac.add((x,y))
            elif PorA == "A":
                if (x,y) in atl:
                    return
                atl.add((x,y))
            visited.add((x,y))

            dfs(x+1,y,heights[x][y], PorA)
            dfs(x-1,y,heights[x][y], PorA)
            dfs(x,y+1,heights[x][y], PorA)
            dfs(x,y-1,heights[x][y], PorA)
            visited.remove((x,y))

        for i in range(row):
            dfs(i,0,0,"P")
            dfs(i,col-1,0,"A")
        for i in range(col):
            dfs(0,i,0,"P")
            dfs(row-1,i,0,"A")


        return pac & atl
