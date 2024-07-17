# https://www.acmicpc.net/problem/14620

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, grid):
    def check(row, col):
        if not (1 <= row < n - 1 and 1 <= col < n - 1):
            return False
        if grid[row - 1][col] < 0 or grid[row + 1][col] < 0 or grid[row][col - 1] < 0 or grid[row][col] < 0 or \
                grid[row][col + 1] < 0:
            return False
        return True

    def convert(row, col):
        total = 0
        total += grid[row + 1][col] + grid[row - 1][col] + grid[row][col - 1] + grid[row][col + 1] + grid[row][col]
        grid[row + 1][col] *= -1
        grid[row - 1][col] *= -1
        grid[row][col - 1] *= -1
        grid[row][col + 1] *= -1
        grid[row][col] *= -1
        return total

    def backtrack(row, col, count, total_cost):
        if count == 3:
            cost[0] = min(cost[0], total_cost)
            for g in grid:
                print(g)
            print(total_cost-15)
            print()
            return
        if col == n - 1:
            row += 1
            col = 0
        if row > n - 2:
            return

        if check(row, col):
            price = convert(row, col)
            backtrack(row, col + 1, count + 1, total_cost + price)
            convert(row, col)
        backtrack(row, col + 1, count, total_cost)

    for row in range(n):
        for col in range(n):
            grid[row][col]+=1
    cost = [float('inf')]
    backtrack(1, 1, 0, 0)
    print(cost[0] - 15)
    return cost[0] - 15


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))
