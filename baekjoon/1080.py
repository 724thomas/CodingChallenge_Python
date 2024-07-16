# https://www.acmicpc.net/problem/1080

'''
1. 아이디어 :
    0,0부터 n-2, m-2까지 돌면서 반전시킨다.
2. 시간복잡도 :
    O( n*m )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, grid, target):
    def convert(row, col):
        for r1 in range(row, row + 3):
            for c1 in range(col, col + 3):
                grid[r1][c1] = "1" if grid[r1][c1] == "0" else "0"

    count = 0
    for row in range(n - 2):
        for col in range(m - 2):
            if grid[row][col] != target[row][col]:
                convert(row, col)
                count += 1

    for row in range(n):
        for col in range(m):
            if grid[row][col] != target[row][col]:
                return -1

    return count


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    grid = list(list(input().strip()) for _ in range(n))  # "0 0 0 0", "0 0 0 0"
    target = list(list(input().strip()) for _ in range(n))
    print(solution(n, m, grid, target))
