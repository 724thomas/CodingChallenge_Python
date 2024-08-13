# https://www.acmicpc.net/problem/21940

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, arr, k, cities):
    time = [[float('inf')] * (n) for _ in range(n)]
    for i in range(n):
        time[i][i] = 0

    for u, v, t in arr:
        time[u-1][v-1] = t

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if time[start][end] > time[start][mid] + time[mid][end]:
                    time[start][end] = time[start][mid] + time[mid][end]

    print(*time, sep='\n')
    ans = []
    cmax = float('inf')

    for mid in range(n):
        max_dist = 0
        for friend in cities:
            goes = time[friend-1][mid]
            come = time[mid][friend-1]
            if goes == float('inf') or come == float('inf'):
                max_dist = float('inf')
                break
            max_dist = max(max_dist, goes + come)

        if max_dist < cmax:
            cmax = max_dist
            ans = [mid+1]
        elif max_dist == cmax:
            ans.append(mid+1)

    return sorted(ans)

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cities = tuple(map(int, input().split()))
    print(*solution(n, m, arr, k, cities))

