# https://www.acmicpc.net/problem/21921

'''
1. 아이디어 :
    슬라이딩 윈도우
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, m, arr):
    counts = defaultdict(int)
    ans = total = sum(arr[:m])
    left = 0
    right = m
    while right < len(arr):
        counts[total] += 1
        ans = max(ans, total)
        total += arr[right]
        right += 1
        total -= arr[left]
        left += 1

    counts[total] += 1
    ans = max(ans, total)


    if not ans:
        print("SAD")
    else:
        print(ans)
        print(counts[ans])


n, m = list(map(int, input().split()))
arr = list(map(int, input().strip().split()))
solution(n, m, arr)


# http://colorscripter.com/s/fOMy9qn