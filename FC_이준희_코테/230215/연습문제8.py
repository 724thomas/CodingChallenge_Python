# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

h, r = map(int, input().split())
nums = sorted([int(input()) for x in range(h)])

result = 0
start = 0
end = nums[-1] - nums[0]
if r == 2:
    print(nums[-1] - nums[0])
    exit()
while start <= end:
    mid = (start + end) // 2
    count = 1
    house = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - house >= mid:
            count += 1
            house = nums[i]
    if count >= r:
        result = mid
        start = mid + 1
    elif count < r:
        end = mid - 1
print(result)
