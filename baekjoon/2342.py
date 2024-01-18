# https://www.acmicpc.net/problem/2342

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

integer_list = [int(num) for num in input().split()]


def solution(nums):
    calc = [
        [1, 2, 2, 2, 2],
        [2, 1, 3, 4, 3],
        [2, 3, 1, 3, 4],
        [2, 4, 3, 1, 3],
        [2, 3, 4, 3, 1]
    ]

    dp = {}

    def dfs(left, right, idx):

        if (left, right, idx) in dp:
            return dp[(left, right, idx)]

        if nums[idx] == 0:
            return 0

        next_num = nums[idx]
        if left == next_num or right == next_num:
            cost = 1 + dfs(left, right, idx + 1)
        else:
            left_move = calc[left][next_num] + dfs(next_num, right, idx + 1)
            right_move = calc[right][next_num] + dfs(left, next_num, idx + 1)
            cost = min(left_move, right_move)

        dp[(left, right, idx)] = cost
        return cost

    return dfs(0, 0, 0)


print(solution(integer_list))
