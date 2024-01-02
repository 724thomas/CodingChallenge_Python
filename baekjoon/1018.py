# https://www.acmicpc.net/problem/1018
def cc(color):
    return "W" if color == "B" else "B"


import sys

n, m = list(map(int, sys.stdin.readline().split()))
chess = []
for i in range(n):
    chess.append([x for x in sys.stdin.readline().rstrip()])

cmin = float('inf')
color = "B"
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        for _ in range(2):
            color = cc(color)
            count = 0
            for a in range(8):
                color = cc(color)
                for b in range(8):
                    color = cc(color)
                    if chess[a + i][b + j] == color:
                        count += 1
            cmin = min(cmin, count)
print(cmin)
