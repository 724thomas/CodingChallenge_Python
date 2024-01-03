# https://www.acmicpc.net/problem/11660 구간 합 구하기 5

'''
1. 아이디어 :
    dp 문제
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, t = list(map(int, input().split()))
grid = list(list(map(int, input().split())) for _ in range(n))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[1][1] = grid[0][0]

for i in range(2, n+1):
    dp[i][1] = dp[i-1][1] + grid[i-1][0]
    dp[1][i] = dp[1][i-1] + grid[0][i-1]
for i in range(2, n+1):
    for j in range(2, n+1):
        dp[i][j] = grid[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]


for _ in range(t):
    x1, y1, x2, y2 = [int(num) for num in input().split()]
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
