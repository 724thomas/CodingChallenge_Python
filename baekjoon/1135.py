# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 / 알고리즘 :

'''


import sys
from collections import defaultdict

#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, parent):
    children = [[] for _ in range(n)]

    for i in range(1, n):
        p = parent[i]
        children[p].append(i)

    def dfs(u):
        if not children[u]:
            return 0

        times = []
        for v in children[u]:
            times.append(dfs(v))

        times.sort(reverse=True)

        ret = 0
        for i, t in enumerate(times, start=1):
            ret = max(ret, t+i)

        return ret

    return dfs(0)


if __name__ == '__main__':
    n = int(input().rstrip())
    arr = tuple(map(int, input().split()))
    print(solution(n, arr))

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