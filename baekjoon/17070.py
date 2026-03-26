# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, grid):
    prefix_sum_prev = [[0,0,0] for _ in range(n)]
    for col in range(n):
        if grid[0][col] == 0:
            prefix_sum_prev[col][0] = 1
        else:
            break
    prefix_sum_prev[0][0] = 0

    for row in range(1, n):
        prefix_sum_next = [[0,0,0] for _ in range(n)]
        for col in range(1,n):
            if grid[row][col] == 1: continue
            # 세로 (위)
            prefix_sum_next[col][1] += prefix_sum_prev[col][1]
            prefix_sum_next[col][1] += prefix_sum_prev[col][2]
            # 가로 (왼)
            prefix_sum_next[col][0] += prefix_sum_next[col-1][0]
            prefix_sum_next[col][0] += prefix_sum_next[col-1][2]
            # 대각 (왼위)
            if grid[row-1][col] == 0 and grid[row][col-1] == 0:
                prefix_sum_next[col][2] += prefix_sum_prev[col-1][0]
                prefix_sum_next[col][2] += prefix_sum_prev[col-1][1]
                prefix_sum_next[col][2] += prefix_sum_prev[col-1][2]
        prefix_sum_prev = prefix_sum_next
    return sum(prefix_sum_prev[n-1])

if __name__ == '__main__':
    n = int(input().rstrip())
    grid = list(list(map(int, input().split())) for _ in range(n))
    print(solution(n, grid))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"