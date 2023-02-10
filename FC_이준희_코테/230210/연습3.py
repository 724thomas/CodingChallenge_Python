# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

dp = [1, 2, 3]
for i in range(47):
    dp.append(dp[-1] + dp[-2] + dp[-3])

print(dp[-1])

