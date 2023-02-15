# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline
nums = []
for _ in range(9):
    nums.append(int(input()))
nums.sort()
target = sum(nums) - 100
candid = []
for num in nums:
    if num not in candid:
        candid.append(target - num)
    else:
        nums.remove(num)
        nums.remove(target - num)
        break

for num in nums:
    print(num)

