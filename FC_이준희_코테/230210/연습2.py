# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

dp = [3, 5, 7]
for i in range(17):
    dp.append(dp[-1] + dp[-3])

print(dp[-1])
