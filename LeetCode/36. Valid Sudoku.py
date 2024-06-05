#

'''
1. 아이디어 :
    row,col,square 체크
2. 시간복잡도 :
    O( 9*9*9 )
3. 자료구조 :
    -
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_valid(x,y):
            target = board[x][y]
            start_x, start_y = (x//3) *3, (y//3) *3
            for i in range(3):
                for j in range(3):
                    if board[start_x+i][start_y+j]!="." and (start_x+i!=x or start_y+j!=y):
                        if board[start_x+i][start_y+j] == target:
                            print(start_x+i, start_y+j)
                            return False

            for i in range(9):
                if board[x][i] == target and i!=y:
                    print(x, i)
                    return False
            for i in range(9):
                if board[i][y] == target and i!=x:
                    print(i, y)
                    return False
            return True


        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    if not check_valid(row, col):
                        print(row,col)
                        return False
        return True