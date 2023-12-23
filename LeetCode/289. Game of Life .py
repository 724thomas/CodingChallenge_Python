#https://leetcode.com/problems/game-of-life/description/

'''
1. 아이디어 :
    바뀌는 위치를 저장할 changed set을 만든다.
    8방향을 탐색하면서, board[new_row][new_col]이 1이면 neighbors를 1 증가시킨다.
    조건에 따라 바뀌면 changed에 저장하고, changed를 돌면서 1인 위치를 0으로, 0인 위치를 1로 바꾼다.
2. 시간복잡도 :
    O(m * n * 8)
3. 자료구조 :

'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = set()
        dir = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]

        for row in range(len(board)):
            for col in range(len(board[0])):
                neighbors = 0
                for row2, col2 in dir:
                    new_row = row+row2
                    new_col = col+col2
                    if 0<=new_row<len(board) and 0<=new_col<len(board[0]) and board[new_row][new_col]:
                        neighbors += 1

                if board[row][col]:
                    if neighbors < 2 or neighbors > 3:
                        changed.add((row,col))
                else:
                    if neighbors == 3:
                        changed.add((row,col))

        for row, col in changed:
            board[row][col] = int(not board[row][col])