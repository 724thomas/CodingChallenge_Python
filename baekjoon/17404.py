# https://www.acmicpc.net/problem/17404

'''
1. 아이디어 :
    DP로 첫번쨰 집을 칠하는 경우의 수 만큼 dp 배열을 만든다.
    dp[0]을 해당 색갈 값으로 초기화
    dp[1] ~ dp[n]까지, cost[i][0] + min(dp[i-1][1], dp[i-1][2]을 구한다.
    마지막 n에서, 첫번쨰 집과 겹치는 값을 제외한 나머지 두 값의 최소값을 구한다.
2. 시간복잡도 :
    O( 3*n*3 )
3. 자료구조
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, costs):
    cmin = float('inf')

    for f_color in range(3):
        dp = [[float('inf')] * 3 for _ in range(n)]

        dp[0][f_color] = costs[0][f_color]

        for i in range(1, n):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

        for l_color in range(3):
            if l_color != f_color:
                cmin = min(cmin, dp[n - 1][l_color])

    return cmin


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))
print(solution(n, grid))
