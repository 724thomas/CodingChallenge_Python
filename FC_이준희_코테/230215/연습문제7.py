# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int, input().split()))
start = 0
end = max(nums)
ans = 0

while start<=end:
    mid = (start+end)//2
    total = sum([x-mid for x in nums if x>mid])

    if total>=m:
        start = mid+1
    elif total<m:
        end = mid-1
print(end)

