# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
nums, cmax = deque([0] * (n + 6)), 0
for i in range(n):
    t, p = map(int, input().split())
    nums[t] = max(nums[t], p + cmax)
    nums.popleft()
    nums.append(0)
    cmax = max(cmax, nums[0])
print(cmax)