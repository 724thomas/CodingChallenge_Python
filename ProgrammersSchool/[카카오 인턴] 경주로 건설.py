# https://school.programmers.co.kr/learn/courses/30/lessons/67259

'''
1. 아이디어 :
    path를 매번 저장하면서 bfs로 풀어보려했는데, 메모리 초과로 실패.

2. 시간복잡도 :

3. 자료구조 :

'''

from collections import deque

def solution(board):
    N = len(board)
    cost = [[float('inf')] * N for _ in range(N)]
    cost[0][0] = 0

    # row, col, previous direction, total cost
    queue = deque([(0, 0, -1, 0)])

    # d u r l
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, col, prev, curr_cost = queue.popleft()

        for i, (row2, col2) in enumerate(directions):
            nrow, ncol = row + row2, col + col2
            if 0 <= nrow < N and 0 <= ncol < N and board[nrow][ncol] == 0:
                if prev == i or prev == -1:
                    new_cost = curr_cost + 100
                else:
                    new_cost = curr_cost + 600

                if cost[nrow][ncol] == float('inf'):
                    cost[nrow][ncol] = new_cost
                    queue.append((nrow, ncol, i, new_cost))

                elif cost[nrow][ncol] >= new_cost:
                    cost[nrow][ncol] = min(new_cost, cost[nrow][ncol])
                    queue.append((nrow, ncol, i, new_cost))
        print(queue)
        for c in cost:
            print(c)

        print()
    return cost[-1][-1]


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board = [[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]
print(solution(board))
