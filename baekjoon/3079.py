# https://www.acmicpc.net/problem/3079

'''
1. 아이디어 :
    힙을 사용하면 시간초과
    이분탐색으로 걸리는 시간초를 구한다.
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    -
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

import heapq


def solution(n, m, arr):
    left, right = 1, max(arr) * m
    ans = right

    while left<=right:
        mid = (left+right)//2
        total_people = sum(mid // time for time in arr)

        if total_people >= m:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    return ans

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = [int(input()) for _ in range(n)]
    print(solution(n, m, arr))
