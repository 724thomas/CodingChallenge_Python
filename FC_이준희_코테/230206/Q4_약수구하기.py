# https://www.acmicpc.net/problem/2501

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
divisors = []
count = 0
for i in range(1, n + 1):
    if n % i == 0 and count < k:
        divisors.append(i)
        count += 1
print(0 if len(divisors) < k else divisors[-1])
