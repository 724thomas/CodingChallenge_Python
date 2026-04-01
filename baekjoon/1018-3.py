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

def solution(n, m, grid):
    ans = float('inf')

    for row in range(n-7):
        for col in range(m-7):
            white = 0
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0 and grid[row + i][col + j] != 'W':
                        white += 1
                    elif (i + j) % 2 == 1 and grid[row + i][col + j] != 'B':
                        white += 1

            ans = min(ans, min(white, 64 - white))
    return ans



if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
    print(solution(n, m, grid))

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