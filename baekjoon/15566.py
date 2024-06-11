# https://www.acmicpc.net/problem/15566

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

import sys
input = sys.stdin.readline

def solution(n, m, topics, frog_pref, edges):
    log = [[-1]*n for _ in range(n)]
    places = [-1]*n
    taken = [-1]*n
    ans = [False]

    def isValid():
        for i in range(n):
            for j in range(n):
                if i != j and log[i][j] != -1:
                    frog1 = places[i]
                    frog2 = places[j]
                    target = log[i][j]
                    if topics[frog1][target] != topics[frog2][target]:
                        return False
        for i in range(n):
            taken[i] = places[i]
        return True

    def recursion(frogindex):
        if frogindex == n:
            if isValid():
                ans[0] = True
                return True
            return False
        for i in range(2):
            tempflower = frog_pref[frogindex][i]
            if places[tempflower] == -1:
                places[tempflower] = frogindex
                if recursion(frogindex + 1):
                    return True
                places[tempflower] = -1
        return False

    for u, v, t in edges:
        log[u][v] = t
        log[v][u] = t

    if recursion(0):
        print("YES")
        print(" ".join(str(x+1) for x in taken))
    else:
        print("NO")

n, m = map(int, input().strip().split())
topics = [list(map(int, input().strip().split())) for _ in range(n)]
frog_pref = [tuple(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(n)]
edges = [tuple(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(m)]

solution(n, m, topics, frog_pref, edges)

