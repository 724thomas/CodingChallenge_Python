# https://leetcode.com/problems/n-queens/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans=[]
        board=[["."] * n for x in range(n)]
        col=set()
        diag=set() #r+c
        adiag=set() #r-c


        def dfs(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r+c) in diag or (r-c) in adiag:
                    continue

                col.add(c)
                diag.add(r+c)
                adiag.add(r-c)
                board[r][c]="Q"

                dfs(r+1)

                col.remove(c)
                diag.remove(r+c)
                adiag.remove(r-c)
                board[r][c]="."


        dfs(0)
        return ans
