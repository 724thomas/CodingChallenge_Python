# https://www.acmicpc.net/problem/2961

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, tastes):
    cmax = [float('inf')]

    def backtrack(a, b, idx, counts):
        if counts != 0:
            cmax[0] = min(cmax[0], abs(a-b))
        if idx == len(tastes):
            return

        a2, b2 = tastes[idx]
        backtrack(a*a2, b+b2, idx+1, counts+1)
        backtrack(a, b, idx+1, counts)



    backtrack(1, 0, 0, 0)
    return cmax[0]

n = int(input())
tastes = []
for _ in range(n):
    tastes.append(list(map(int, input().strip().split())))
print(solution(n, tastes))


