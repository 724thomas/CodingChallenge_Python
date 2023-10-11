# https://leetcode.com/problems/n-queens-ii/description/

'''
1. 아이디어 :
    백트래킹으로 풀 수 있다.
    valid 한걸 체크하는 기능이 까다로운데,
    negDiag는 row-col을 하면 -대각선 값은 항상 같은 값이 나오고,
    posDiag는 row+col을 하면 +대각선 값은 항상 같은 값이 나온다.
2. 시간복잡도 :
    O(n!)
3. 자료구조 :
    해시셋
'''

class Solution:
    def totalNQueens(self, n: int) -> int:

        col = set()
        posDiag = set()
        negDiag = set()

        self.res = 0

        def backtrack(r):
            if r == n:
                self.res+=1
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        backtrack(0)
        return self.res