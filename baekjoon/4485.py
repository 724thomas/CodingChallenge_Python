# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
import heapq
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()
dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def solution(n, grid):
    cache = [[float('inf') for _ in range(n)] for _ in range(n)]
    cache[0][0] = grid[0][0]

    pq = [] # cost, x, y
    heapq.heappush(pq, (grid[0][0], 0, 0))

    while len(pq) > 0:
        cost, x, y = heapq.heappop(pq)
        if (x, y) == (n-1, n-1): return cost
        if cost != cache[x][y]: continue

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            new_cost = cost + grid[nx][ny]
            if new_cost >= cache[nx][ny]: continue
            cache[nx][ny] = new_cost
            heapq.heappush(pq, (new_cost, nx, ny))
    return -1


if __name__ == '__main__':
    count = 0
    while True:
        count+=1
        n = int(input())
        if n == 0: break
        grid = list(list(map(int, input().split())) for _ in range(n))
        print("Problem " + str(count) + ": " + str(solution(n, grid)))

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