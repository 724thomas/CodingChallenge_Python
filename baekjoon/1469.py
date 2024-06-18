# https://www.acmicpc.net/problem/1469

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, nums):
    nums.sort()
    arr = [-1] * (n*2)
    visited = set()

    def backtrack(idx):
        if idx == 2*n:
            print(*arr)
            exit()

        if arr[idx] != -1:
            backtrack(idx+1)
            return

        for num in nums:
            if num in visited:
                continue

            pair_idx = idx + num + 1
            if pair_idx < 2 * n and arr[pair_idx] == -1:
                arr[idx] = num
                arr[pair_idx] = num
                visited.add(num)

                backtrack(idx+1)

                arr[idx] = -1
                arr[pair_idx] = -1
                visited.remove(num)

    backtrack(0)
    print(-1)


counts = int(input())
arr = list(map(int, input().strip().split()))
solution(counts, arr)
