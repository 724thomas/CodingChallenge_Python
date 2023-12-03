# https://school.programmers.co.kr/learn/courses/30/lessons/67259

'''
1. 아이디어 :
    path를 매번 저장하면서 bfs로 풀어보려했는데, 메모리 초과로 실패.
    Memoization으로 했을 시, 테스트 케이스 실패
    row,col에 방향별 cost를 저장하는 방식으로 푼다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열, 큐
'''

from collections import deque


def solution(board):
    cost = [[[float('inf')] * 4 for _ in range(len(board))] for _ in range(len(board))]
    for i in range(4):
        cost[0][0][i] = 0

    # row, col, previous direction, total cost
    queue = deque([(0, 0, -1, 0)])

    # d u r l
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, col, prev, curr_cost = queue.popleft()

        for new_direction, (row2, col2) in enumerate(directions):
            nrow, ncol = row + row2, col + col2
            if 0 <= nrow < len(board) and 0 <= ncol < len(board) and board[nrow][ncol] == 0:
                if prev == new_direction or prev == -1:
                    new_cost = curr_cost + 100
                else:
                    new_cost = curr_cost + 600

                if cost[nrow][ncol][new_direction] > new_cost:
                    cost[nrow][ncol][new_direction] = new_cost
                    queue.append((nrow, ncol, new_direction, new_cost))

    return min(cost[-1][-1])
