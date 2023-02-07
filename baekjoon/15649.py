# https://www.acmicpc.net/problem/15649

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
res = []


def dfs2():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    for i in range(len(nums)):
        n = nums.pop(i)
        res.append(n)
        dfs2()
        res.pop()
        nums.insert(i, n)
dfs2()

def dfs():
    if len(res) == m:
        print(' '.join(map(str,res)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        res.append(i)
        dfs()
        res.pop()
        visited[i] = False

visited = [False] * (n + 1)
dfs()





print(res)