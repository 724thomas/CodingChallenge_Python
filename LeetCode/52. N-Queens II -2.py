# https://leetcode.com/problems/n-queens-ii/description/

'''
1. 아이디어 :
    양의 대각선, 음의 대각선, 열을 set으로 만들어서 퀸이 놓일 수 있는지 확인한다.
    퀸이 놓일 수 있으면 다음 행으로 넘어간다.
2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        pos_diag = set()
        neg_diag = set()
        column = set()

        ans = [0]

        def backtrack(idx, row, col):
            if row-col in neg_diag:
                return False
            if row+col in pos_diag:
                return False
            if col in column:
                return False

            if idx == n-1:
                ans[0] += 1
                return

            neg_diag.add(row-col)
            pos_diag.add(row+col)
            column.add(col)

            for i in range(n):
                backtrack(idx+1, row+1, i)

            neg_diag.remove(row-col)
            pos_diag.remove(row+col)
            column.remove(col)

        for i in range(n):
            backtrack(0, 0, i)

        return ans[0]



