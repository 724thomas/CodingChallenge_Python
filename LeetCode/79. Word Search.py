#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [ [0,-1], [0,1], [-1,0], [1,0] ]
        ans = [False]
        def backtrack(row1, col1, idx):
            if idx == len(word):
                return True

            if not (0 <= row1 < len(board) and 0 <= col1 < len(board[0])):
                return False
            if board[row1][col1] != word[idx]:
                return False

            temp = board[row1][col1]
            board[row1][col1] = '-1'


            for row2, col2 in dir:
                nrow, ncol =row1+row2, col1+col2
                if backtrack(nrow, ncol, idx + 1):
                    return True

            board[row1][col1] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and backtrack(row, col, 0):
                    return True

        return False

