# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

dp = [2, 4]
for i in range(5):
    dp.append(dp[-1] + dp[-2])
print(dp[-1])
