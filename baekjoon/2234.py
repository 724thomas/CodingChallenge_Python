# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''
from collections import defaultdict, deque

def solution(n, temp_arr):
    # 1: Up,   2: Down,   3: Left,   4: Right
    def get_dir(curr_dir, block):
        if block == 0:
            return curr_dir
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

    direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

    # make new arr
    arr = [[5] * (n + 2)]
    for i in range(n):
        arr.append([5] + temp_arr[i] + [5])
    arr.append(([5] * (n + 2)))

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

    def bfs(start_x, start_y, start_dir):
        queue = deque([(start_x, start_y, start_dir, 0)])
        cache = {}
        visited = set()
        max_score = 0

        while queue:
            x, y, dir, score = queue.popleft()

            if (x, y) in blackhole:
                max_score = max(max_score, score)
                continue

            if (x, y, dir) in cache and cache[(x, y, dir)] >= score:
                continue

            cache[(x, y, dir)] = score

            curr = arr[x][y]
            if curr == 0:
                dir2 = dir
            elif 1 <= curr <= 5:
                dir2 = get_dir(dir, curr)
                score += 1
            else:
                x, y = whitehole_map[(x, y)]
                dir2 = dir

            dx, dy = direction[dir2]
            next_x, next_y = x + dx, y + dy

            if (next_x, next_y) == (start_x, start_y):
                max_score = max(max_score, score)
            else:
                queue.append((next_x, next_y, dir2, score))

        return max_score

    max_score = 0
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if arr[row][col] == 0:
                for d in range(1, 5):
                    # max_score = max(max_score, dfs(row, col, row, col, d, 0, False))
                    max_score = max(max_score, bfs(row, col, d))
    return max_score

for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{t + 1} {solution(n, arr)}")




'''
3
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
6
1 1 1 1 1 1
1 1 -1 1 1 1
1 -1 0 -1 1 1
1 1 -1 1 1 1
1 1 1 1 1 1
1 1 1 1 1 1
8
0 0 0 3 0 0 0 0
0 0 2 0 0 5 0 0
0 0 5 0 3 0 0 0
0 0 1 1 0 0 0 4
0 0 0 0 0 0 0 0
0 0 0 0 0 0 5 0
0 0 4 0 0 3 1 0
2 0 0 4 3 4 0 0
'''