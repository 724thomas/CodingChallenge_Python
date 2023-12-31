# https://school.programmers.co.kr/learn/courses/30/lessons/1844 게임 맵 최단거리

'''
1. 아이디어 :
    bfs를 사용해서, row, col, moves를 추적한다.
2. 시간복잡도 :
    O(n*m)
3. 자료구조 :
    해시셋, 큐
'''

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    queue.append((0, 0, 1))
    visited = set()
    visited.add((0, 0))

    dir = [1, 0], [-1, 0], [0, 1], [0, -1]

    while queue:
        row1, col1, moves = queue.popleft()
        if row1 == n - 1 and col1 == m - 1:
            return moves

        for row2, col2 in dir:
            nrow = row1 + row2
            ncol = col1 + col2
            if 0 <= nrow < n and 0 <= ncol < m and maps[nrow][ncol] == 1:
                if (nrow, ncol) not in visited:
                    queue.append((nrow, ncol, moves + 1))
                    visited.add((nrow, ncol))
    return -1
