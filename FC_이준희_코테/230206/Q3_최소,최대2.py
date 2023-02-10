# https://www.acmicpc.net/problem/20065

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

for _ in range(int(input())):
    input()
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    print(nums[0], nums[-1])
