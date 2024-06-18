# https://www.acmicpc.net/problem/5547

'''
1. 아이디어 :
    연산을 편하게하기 위해 양쪽,위아래 0을 추가한다.
    0,0 부터 시작하여(추가한거라 항상 0) bfs를 돈다.
    bfs를 돌면서 주변에 1이 있는지 확인한후에, 그 주변을 큐에 넣는다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시셋, 배열, 해시맵

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque


def solution(w, h, houses):
    dir_even_idx = ((-1, 0), (-1, 1), (0, -1), (0, +1), (1, 0), (1, 1))
    dir_odd_idx = ((-1, -1), (-1, 0), (0, -1), (0, +1), (1, -1), (1, 0))
    dir_idx = {0: dir_odd_idx, 1: dir_even_idx}

    counter = 0
    visited = set()
    visited.add((0, 0))
    queue = deque()
    queue.append((0, 0))

    while queue:
        x1, y1 = queue.popleft()

        for x2, y2 in dir_idx[x1 % 2]:
            x, y = x1 + x2, y1 + y2
            if x < 0 or x >= h or y < 0 or y >= w:
                continue

            if houses[x][y] == 1:
                counter += 1
            if (x, y) in visited or houses[x][y] == 1:
                continue
            visited.add((x, y))
            queue.append((x, y))
    return counter


w, h = list(map(int, input().strip().split()))
houses = []
houses.append([0] * w + [0, 0])
for _ in range(h):
    houses.append([0] + list(map(int, input().strip().split())) + [0])
houses.append([0] * w + [0, 0])
print(solution(w + 2, h + 2, houses))
