# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(n, grid):
    prev = [[0,0,0] for _ in range(n)]
    for col in range(n):
        if grid[0][col] == 0:
            prev[col][0] = 1
        else:
            break
    prev[0][0] = 0

    for row in range(1, n):
        next = [[0,0,0] for _ in range(n)]
        for col in range(1,n):
            if grid[row][col] == 1: continue
            next[col][1] += prev[col][1] + prev[col][2]
            next[col][0] += next[col-1][0] + next[col-1][2]
            if grid[row-1][col] + grid[row][col-1] != 0: continue
            next[col][2] += prev[col-1][0] + prev[col-1][1] + prev[col-1][2]
        prev = next
    return sum(prev[n-1])

if __name__ == '__main__':
    n = int(input().rstrip())
    grid = list(list(map(int, input().split())) for _ in range(n))
    print(solution(n, grid))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"