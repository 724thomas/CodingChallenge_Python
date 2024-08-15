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

from collections import defaultdict


def solution(n, temp_arr):
    # 1: Up,   2: Down,   3: Left,   4:Right
    def get_dir(curr_dir, block):
        if block == 0:
            if curr_dir == 1:
                return 1
            elif curr_dir == 2:
                return 2
            elif curr_dir == 3:
                return 3
            else:
                return 4
        elif block == 1:
            if curr_dir == 1:
                return 2
            elif curr_dir == 2:
                return 4
            elif curr_dir == 3:
                return 1
            else:
                return 3
        elif block == 2:
            if curr_dir == 1:
                return 4
            elif curr_dir == 2:
                return 1
            elif curr_dir == 3:
                return 2
            else:
                return 3
        elif block == 3:
            if curr_dir == 1:
                return 3
            elif curr_dir == 2:
                return 1
            elif curr_dir == 3:
                return 4
            else:
                return 2
        elif block == 4:
            if curr_dir == 1:
                return 2
            elif curr_dir == 2:
                return 3
            elif curr_dir == 3:
                return 4
            else:
                return 1
        elif block == 5:
            if curr_dir == 1:
                return 2
            elif curr_dir == 2:
                return 1
            elif curr_dir == 3:
                return 4
            else:
                return 3

    direction = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

    # make new arr
    arr = []
    arr.append(([5] * (n + 2)))
    for i in range(n):
        arr.append([5] + temp_arr[i] + [5])
    arr.append(([5] * (n + 2)))
    print(*arr, sep='\n')

    # blackhole, whitehole
    blackhole = set()
    whitehole_idx = defaultdict()
    whitehole_map = defaultdict()
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if arr[row][col] == -1:
                blackhole.add((row, col))
            if arr[row][col] >= 6:
                val = arr[row][col]
                if val not in whitehole_idx:
                    whitehole_idx[val] = (row, col)
                else:
                    enter = whitehole_idx[val]
                    exit = (row, col)
                    whitehole_map[enter] = exit
                    whitehole_map[exit] = enter
    print(blackhole)
    print(whitehole_map)

    cache = defaultdict() # x, y, dir
    def dfs(sx, sy, x, y, dir, score, flag):
        if (x, y, dir) in cache:
            return cache[(x, y, dir)]
        if (x, y) in blackhole:
            return score
        if x == sx and y == sy and flag:
            return score

        flag = True
        curr = arr[x][y]

        if curr == 0:
            dir2 = get_dir(dir, curr)
            x2, y2 = direction[dir2]
            score = dfs(sx, sy, x + x2, y + y2, dir2, score, flag)
        elif 1 <= curr <= 5:
            dir2 = get_dir(dir, curr)
            x2, y2 = direction[dir2]
            score = dfs(sx, sy, x + x2, y + y2, dir2, score + 1, flag)
        else:
            x2, y2 = whitehole_map[(x, y)]
            score = dfs(sx, sy, x2, y2, dir, score, flag)

        cache[(x,y,dir)] = max(cache[(x,y,dir)], score)
        return score

    ans = 0
    for row in range(1, n):
        for col in range(1, n):
            ans = min(ans, dfs(row, col, row, col, 1, 0, False))
            ans = min(ans, dfs(row, col, row, col, 2, 0, False))
            ans = min(ans, dfs(row, col, row, col, 3, 0, False))
            ans = min(ans, dfs(row, col, row, col, 4, 0, False))
    return ans


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        print(solution(n, arr))

'''
1
10
0 1 0 3 0 0 0 0 7 0
0 0 0 0 -1 0 5 0 0 0
0 4 0 0 0 3 0 0 2 2
1 0 0 0 1 0 0 3 0 0
0 0 3 0 0 0 0 0 6 0
3 0 0 0 2 0 0 1 0 0
0 0 0 0 0 1 0 0 4 0
0 5 0 4 1 0 7 0 0 5
0 0 0 0 0 1 0 0 0 0
2 0 6 0 0 4 0 0 0 4
'''
