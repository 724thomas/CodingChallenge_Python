# https://leetcode.com/problems/surrounded-regions/

'''
1. 아이디어 :
    dfs
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        dir = ((1,0), (-1,0), (0,1), (0,-1))

        def change_area(area, before, after, rows, cols):
            if area == "edges":

                for row in range(rows):
                    if board[row][0] == before:
                        dfs(row, 0, before, after)
                    if board[row][cols-1] == before:
                        dfs(row, cols-1, before, after)

                for col in range(cols):
                    if board[0][col] == before:
                        dfs(0, col, before, after)
                    if board[rows-1][col] == before:
                        dfs(rows-1, col, before, after)
            else:
                for row in range(rows):
                    for col in range(cols):
                        if board[row][col] == before:
                            dfs(row, col, before, after)


        def dfs(row1, col1, before, after):
            board[row1][col1] = after

            for row2, col2 in dir:
                nrow = row1+row2
                ncol = col1+col2
                if 0<=nrow<rows and 0<=ncol<cols and board[nrow][ncol] == before:
                    print(nrow, ncol)
                    dfs(nrow, ncol, before, after)

        change_area("edges", "O", "A", rows, cols)
        change_area("all","O", "X", rows, cols)
        change_area("edges", "A", "O", rows, cols)
