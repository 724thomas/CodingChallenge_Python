# https://www.acmicpc.net/problem/16719

'''
1. 아이디어 :
    재귀로 풀 수 있다.
2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys

input = sys.stdin.readline


def solution(arr):

    def dfs(start, divided_arr):
        if not divided_arr:
            return
        min_char = min(divided_arr)
        min_idx = divided_arr.index(min_char)

        result[start + min_idx] = min_char

        print("".join(result))

        dfs(start + min_idx + 1, divided_arr[min_idx + 1:])
        dfs(start, divided_arr[:min_idx])

    result = [""] * len(arr)
    dfs(0, arr)


arr = list(input().rstrip())
solution(arr)
