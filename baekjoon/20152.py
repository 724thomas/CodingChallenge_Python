# https://www.acmicpc.net/problem/20152

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(H, N):
    if H == N:
        return 1
    if H > N:
        N, H = H, N
    N -= H - 1

    dp = [[0 for _ in range(N)] for _ in range(N)]

    dp[0][0] = 1
    for i in range(N):
        dp[0][i] = 1

    for row in range(1, N):
        for col in range(1, N):
            if row > col:
                continue
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[-1][-1]


H, N = list(map(int, input().split()))
print(solution(H, N))
