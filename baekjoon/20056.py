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


def solution(n, m, k, fireballs):
    # r, c, m, s, d = r,c, 질량, 속력, 방향
    # print(*fireballs, sep="\n")

    dirs = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}

    def fireball_move(fireballs):
        cords = defaultdict(list)

        for row, col, mass, speed, dir in fireballs:
            nr = (row + dirs[dir][0] * speed) % n
            nc = (col + dirs[dir][1] * speed) % n
            cords[(nr, nc)].append((mass, speed, dir))
        return cords

    def split(cords):
        fireballs = []

        for (row, col), vals in cords.items():
            if len(vals) == 1:
                fireballs.append(((row, col) + vals[0]))
            else:
                total_mass = total_speed = 0
                for mass, speed, _ in vals:
                    total_mass += mass
                    total_speed += speed
                mass = total_mass // 5
                if mass == 0: continue
                speed = total_speed // len(vals)

                all_even = all(direction % 2 == 0 for _, _, direction in vals)
                all_odd = all(direction % 2 == 1 for _, _, direction in vals)

                if all_even or all_odd:
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]

                for d in directions:
                    fireballs.append((row, col, mass, speed, d))
        return fireballs

    for _ in range(k):
        cords = fireball_move(fireballs)
        fireballs = split(cords)

    return sum([m for r, c, m, s, d in fireballs])


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, k, arr))
