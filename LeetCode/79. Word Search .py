# https://leetcode.com/problems/word-search/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        board_total = defaultdict(int)

        for row in range(len(board)):
            for col in range(len(board[0])):
                board_total[board[row][col]]+=1
        word_total = Counter(word)
        for k, v in word_total.items():
            if board_total[k] < v:
                return False
        visited=set()

        self.ans=False

        def backtrack(row,col,idx):
            if self.ans:
                return
            if idx>=len(word):
                self.ans=True
                return
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or word[idx]!=board[row][col] or (row,col) in visited:
                return

            temp = board[row][col]
            board[row][col] = "/"

            for row2, col2 in dir:
                nrow=row+row2
                ncol=col+col2
                if (nrow, ncol) not in visited:
                    backtrack(nrow, ncol, idx+1)

            board[row][col] = temp

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    backtrack(row,col,0)


        return self.ans