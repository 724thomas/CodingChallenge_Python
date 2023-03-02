# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys
input = sys.stdin.readline

locs = int(input())
nums = list(map(int, input().split()))
target = int(input())
if sum(nums) <= target:
    print(max(nums))
    exit()
start = 0
end = max(nums)
while start <= end:
    mid = (start + end) // 2
    if sum([i if i < mid else mid for i in nums]) <= target:
        start = mid + 1
    else:
        end = mid - 1
print(end)
