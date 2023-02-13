# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
curr = cmax = nums[0]

for i in range(1, len(nums)):
    curr = max(nums[i], nums[i] + curr)
    cmax = max(cmax, curr)

print(cmax)

