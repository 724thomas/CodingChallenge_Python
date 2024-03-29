# https://www.acmicpc.net/problem/25916

'''
1. 아이디어 :
    1) 연속된 최대합을 구하는 문제다. 투포인터로 풀 수 있다. while문 rp가 오른쪽 끝까지 갈때까지
    안에서 lp[0], lp[1]로 target보다 작으면 lp+=1, 아니면 rp+=1, 같으면 lp+=1, rp+=1로 풀 수 있다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
n, target= map(int, input().split())
nums = list(map(int, input().split()))
cmax, total, lp, rp = 0, nums[0], 0, 0
while rp < n - 1:
    if total < target:
        rp += 1
        total += nums[rp]
    elif total > target:
        total -= nums[lp]
        lp += 1
    elif total == target:
        rp += 1
        total += nums[rp]
        total -= nums[lp]
        lp += 1
    if total <= target:
        cmax = max(cmax, total)
print(cmax)
