# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

n = int(input())
dp=[0,1]
for i in range(n-1):
    dp.append(dp[-1]+dp[-2])

print(dp[-1])