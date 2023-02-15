# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
nums = [int(x * (x + 1) / 2) for x in range(1, 1000) if int(x * (x + 1) / 2) <= 1000]
possible_num = set()
for i in nums:
    for j in nums:
        for k in nums:
            if (i + j + k) <= 1000 and i + j + k not in possible_num:
                possible_num.add(i + j + k)
for _ in range(int(input())):
    print(1 if int(input()) in possible_num else 0)

