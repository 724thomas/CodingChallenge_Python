# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys
n = int(sys.stdin.readline())
dp = [1, 2]
for i in range(n - 2):
    dp.append(dp[-1] + dp[-2])
print(dp[n - 1] % 10007)

