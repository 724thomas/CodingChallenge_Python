# https://www.acmicpc.net/problem/

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


def solution(n, m, q_arr, k_arr, p_arr):
    arr = [[0 for _ in range(m)] for _ in range(n)]

    knight_dir = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    queen_dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for i in range(1, len(k_arr), 2):
        x, y = k_arr[i] - 1, k_arr[i + 1] - 1
        arr[x][y] = 1
        for x2, y2 in knight_dir:
            nx, ny = x + x2, y + y2
            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
                continue
            arr[nx][ny] = 2

    for i in range(1, len(p_arr), 2):
        x, y = p_arr[i] - 1, p_arr[i + 1] - 1
        arr[x][y] = 1


    for i in range(1, len(q_arr), 2):
        x, y = q_arr[i] - 1, q_arr[i + 1] - 1
        arr[x][y] = 1

        for x2, y2 in queen_dir:
            nx, ny = x, y
            while True:
                nx += x2
                ny += y2
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                if arr[nx][ny] == 1:
                    break
                arr[nx][ny] = 2

    ans = 0
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 0:
                ans += 1

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    q_arr = tuple(map(int, input().split()))
    k_arr = tuple(map(int, input().split()))
    p_arr = tuple(map(int, input().split()))
    print(solution(n, m, q_arr, k_arr, p_arr))

'''
5 7
1 2 3
0
0
'''
