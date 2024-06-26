# https://www.acmicpc.net/problem/1890

'''
1. 아이디어 :
    dp 문제
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys
input = sys.stdin.readline

def solution(n, grid):
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if dp[i][j] != 0 and grid[i][j] != 0:
                jump = grid[i][j]

                if i + jump < n:  # 아래쪽으로 점프
                    dp[i + jump][j] += dp[i][j]

                if j + jump < n:  # 오른쪽으로 점프
                    dp[i][j + jump] += dp[i][j]

    return dp[n - 1][n - 1]  # 마지막 칸에 저장된 경로의 수 반환


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
print(solution(n, grid))