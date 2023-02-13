# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
dp = {1: 1, 2: 1, 3: 1}
for i in range(int(input())):
    n = int(input())
    for i in range(4, n+1):
        if i not in dp:
            dp[i] = (dp[i - 2] + dp[i - 3])
    print(dp[n])

