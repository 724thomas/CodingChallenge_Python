# https://www.acmicpc.net/problem/18430

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, m, mat):
    dir = [[(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0, -1), (1, 0)]]

    def check(idx, x1, y1):
        if taken[x1][y1]:
            return False
        neighbors = dir[idx]
        for dx, dy in neighbors:
            nx, ny = x1 + dx, y1 + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or taken[nx][ny]:
                return False
        return True

    def place_boomerang(idx, x1, y1):
        temp = mat[x1][y1] * 2
        taken[x1][y1] = True
        for dx, dy in dir[idx]:
            nx, ny = x1 + dx, y1 + dy
            temp += mat[nx][ny]
            taken[nx][ny] = True
        return temp

    def remove_boomerang(idx, x1, y1):
        taken[x1][y1] = False
        for dx, dy in dir[idx]:
            nx, ny = x1 + dx, y1 + dy
            taken[nx][ny] = False

    def backtrack(x1, y1, current_sum):
        if x1 == n:
            nonlocal max_sum
            max_sum = max(max_sum, current_sum)
            return

        nx, ny = (x1, y1 + 1)
        if ny == m:
            nx += 1
            ny = 0

        if not taken[x1][y1]:
            for i in range(len(dir)):
                if check(i, x1, y1):
                    temp = place_boomerang(i, x1, y1)
                    backtrack(nx, ny, current_sum + temp)
                    remove_boomerang(i, x1, y1)

        backtrack(nx, ny, current_sum)

    taken = [[False] * m for _ in range(n)]
    max_sum = 0
    backtrack(0, 0, 0)
    return max_sum

n, m = map(int, input().strip().split())
mat = [list(map(int, input().strip().split())) for _ in range(n)]

print(solution(n, m, mat))
