#https://leetcode.com/problems/word-search/description/

'''
1. 아이디어 :
    dfs로 풀 수 있다.
2. 시간복잡도 :
    (row * col * 4^len(word))
    2차 배열의 모든 알파뱃을 확인하는 작업(row*col) * 4 방향으로 dfs 호출
3. 자료구조 :
    배열
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        path = set()

        def dfs(r, c, pos):
            if pos==len(word):
                return True
            if (r<0 or c<0 or
                    r>=row or c>=col or
                    word[pos]!=board[r][c] or
                    (r,c)==1):
                return False

            temp = board[r][c]
            board[r][c]=1
            res = (dfs(r+1, c, pos+1) or
                   dfs(r-1, c, pos+1) or
                   dfs(r, c+1, pos+1) or
                   dfs(r, c-1, pos+1))
            board[r][c]=temp
            return res

        for r in range(row):
            for c in range(col):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
        return False



