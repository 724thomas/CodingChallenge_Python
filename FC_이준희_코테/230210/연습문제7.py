# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import math
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = sys.maxsize
            for k in range(j - i):
                small = min(small, dp[i][i + k] + dp[i + k + 1][j])  # 경우의 수들 중 최소값
            dp[i][j] = small + sum(arr[i:j + 1])  # i~ j+1까지 합
    print (dp[0][-1])



import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dp = [[0] * n for _ in range(n)]
    f = list(map(int, input().split()))
    s = [0]
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = i
        s.append(s[i]+f[i])

    for z in range(1, n):
        for i in range(n-z):
            j = i + z
            dp[i][j]=sys.maxsize

            for k in range(A[i][j - 1], min(A[i + 1][j]+1,j)):
                minn = dp[i][k]+dp[k+1][j]+s[j+1]-s[i]
                if dp[i][j]>minn:
                    dp[i][j]=minn
                    A[i][j] = k
    print(dp[0][-1])

