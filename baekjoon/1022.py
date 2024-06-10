# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
def calculate_value(x, y):
    layer = max(abs(x), abs(y))
    if y == -layer:
        return (2 * layer - 1) ** 2 + (layer - x)
    elif x == layer:
        return (2 * layer - 1) ** 2 + (2 * layer) + (layer - y)
    elif y == layer:
        return (2 * layer - 1) ** 2 + 2 * (2 * layer) + (x + layer)
    else:
        return (2 * layer - 1) ** 2 + 3 * (2 * layer) + (y + layer)

def solution(r1, c1, r2, c2):
    rows = r2 - r1 + 1
    cols = c2 - c1 + 1
    grid = [[0] * cols for _ in range(rows)]
    max_val_length = 0

    for i in range(rows):
        for j in range(cols):
            x, y = r1 + i, c1 + j
            grid[i][j] = calculate_value(x, y)
            max_val_length = max(max_val_length, len(str(grid[i][j])))

    result = []
    for row in grid:
        formatted_row = ' '.join(f"{val:>{max_val_length}}" for val in row)
        result.append(formatted_row)

    return '\n'.join(result)

# 입력 처리
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
r1, c1, r2, c2 = list(map(int, input().split()))
print(r1, c1, r2, c2)

# 결과 출력
print(solution(r1, c1, r2, c2))
