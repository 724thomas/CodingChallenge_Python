# https://leetcode.com/problems/valid-sudoku/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_valid(x,y):
            target = board[x][y]
            start_x, start_y = (x//3) *3, (y//3) *3
            for i in range(3):
                for j in range(3):
                    if board[start_x+i][start_y+j]!="." and (start_x+i!=x and start_y+j!=y):
                        if board[start_x+i][start_y+j] == target:
                            return False

            for i in range(9):
                if board[x][i] == target and i!=y:
                    return False
            for i in range(9):
                if board[i][y] == target and i!=x:
                    return False
            return True


        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    if not check_valid(row, col):
                        return False
        return True