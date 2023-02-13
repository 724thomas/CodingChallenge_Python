# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
n = int(sys.stdin.readline())
dp = {1:1, 2:2}
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[n])

