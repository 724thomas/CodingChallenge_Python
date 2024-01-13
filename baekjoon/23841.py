# https://www.acmicpc.net/problem/23841 데칼코마니

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = grid[i][-1-j]

    return grid

n, m = list(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(n)]

for a in solution(grid):
    print("".join(a))
