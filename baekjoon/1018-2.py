# https://www.acmicpc.net/problem/1018 체스판 다시 칠하기

'''
1. 아이디어 :
    브루트 포스로 풀었다
2. 시간복잡도 :
    O(n*m)
3. 자료구조 :
    배열
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(row, col, grid):
    def change_color(color):
        return "B" if color == "W" else "W"

    def min_count_colors(x, y):
        color = "B"
        for _ in range(2):
            count = 0
            color = change_color(color)
            for i in range(8):
                color = change_color(color)
                for j in range(8):
                    color = change_color(color)
                    if grid[x + i][y + j] != color:
                        count += 1
            min_ans[0] = min(min_ans[0], count)

    min_ans = [float('inf')]
    for i in range(row-8+1):
        for j in range(col-8+1):
            min_count_colors(i,j)

    return min_ans[0]

row, col = list(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(row)]  # "aaa" "bbb"
print(solution(row,col, grid))
