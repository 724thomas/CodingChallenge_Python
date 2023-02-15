# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if (i ** 2 + j ** 2 + m) % (i * j) == 0:
                count += 1
    print(count)
