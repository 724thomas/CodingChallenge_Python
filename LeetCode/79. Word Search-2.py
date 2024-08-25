#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque, defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # print(*board, sep='\n')
        n = len(board)
        m = len(board[0])

        #최적화
        if len(word) > n*m:
            return False

        board_char_count = defaultdict(int)
        for row in range(n):
            for col in range(m):
                board_char_count[board[row][col]] += 1

        word_char_count = defaultdict(int)
        for c in word:
            word_char_count[c] += 1
        for k, v in word_char_count.items():
            if board_char_count[k] < v:
                return False

        if board_char_count[word[0]] > board_char_count[word[-1]]:
            word = word[::-1]


        dir = [[0,1],[0,-1],[1,0],[-1,0]]


        def backtrack(x, y, size):
            if size == len(word):
                return True

            temp = board[x][y]
            board[x][y] = "#"

            for x2, y2 in dir:
                nx, ny = x+x2, y+y2
                if not (0<=nx<n and 0<=ny<m) or board[nx][ny] != word[size]:
                    continue
                if backtrack(nx, ny, size+1):
                    return True
            board[x][y] = temp
            return False

        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0] and backtrack(row, col, 1):
                    return True
        return False


