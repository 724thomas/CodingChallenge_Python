#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count=0

        def dfs(x,y):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or board[x][y]==".":
                return
            board[x][y]='.'
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    dfs(i,j)
                    count+=1
        return count