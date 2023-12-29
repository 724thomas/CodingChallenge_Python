# https://www.acmicpc.net/problem/7576

'''
1. 아이디어 :
    bfs를 돌면서 next와 ripe_apple을 갱신한다.
    apples[i][j]에 0 이 있으면 -1, 없으면 count-1을 리턴
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    큐
'''
from collections import deque
import sys

input = sys.stdin.readline

col, row = map(int, input().split())

apples = []
for _ in range(row):
    apples.append(list(map(int, input().split())))


ripe_apple = deque()
yet_apple = 0
for i in range(row):
    for j in range(col):
        curr = apples[i][j]
        if curr == 0:
            yet_apple += 1
        elif curr == 1:
            ripe_apple.append((i, j))


dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
count = -1
next_apple = deque()
while ripe_apple or next_apple:
    while ripe_apple:
        row1, col1 = ripe_apple.popleft()

        for row2, col2 in dir:
            nrow = row1 + row2
            ncol = col1 + col2
            if 0 <= nrow < row and 0 <= ncol < col and apples[nrow][ncol] == 0:
                next_apple.append((nrow, ncol))
                apples[nrow][ncol] = 1

    for cords in next_apple:
        ripe_apple.append(cords)
    next_apple = []
    count += 1

for i in range(row):
    for j in range(col):
        if apples[i][j] ==0:
            print(-1)
            exit(0)
print(count)
