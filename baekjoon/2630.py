# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, grid):
    prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for row in range(1, n+1):
        for col in range(1, n+1):
            prefix[row][col] = prefix[row-1][col] + prefix[row][col-1] - prefix[row-1][col-1] + grid[row-1][col-1]

    # print(*prefix, sep='\n')

    def dfs(row, col, size):
        total = prefix[row+size][col+size] - prefix[row][col+size] - prefix[row+size][col] + prefix[row][col]
        if total == 0:
            return 1, 0
        elif total == size*size:
            return 0, 1
        else:
            half = size // 2
            white1, blue1 = dfs(row, col, half)
            white2, blue2 = dfs(row, col + half, half)
            white3, blue3 = dfs(row + half, col, half)
            white4, blue4 = dfs(row + half, col + half, half)
            return white1 + white2 + white3 + white4, blue1 + blue2 + blue3 + blue4

    return dfs(0, 0, n)



if __name__ == '__main__':
    n = int(input().rstrip())
    grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
    ans = solution(n, grid)
    print(*ans, sep='\n')

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) fo.r num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"