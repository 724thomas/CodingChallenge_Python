# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted([int(input()) for x in range(n)])

ans = sys.maxsize
lp, rp = 0, 1
while rp < n:
    diff = nums[rp] - nums[lp]
    if diff == m:
        print(m)
        exit()
    elif diff < m:
        rp += 1
    elif diff > m:
        ans = min(ans, diff)
        lp += 1
print(ans)

