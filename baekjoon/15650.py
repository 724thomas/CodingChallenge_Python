# https://www.acmicpc.net/problem/15650

'''
1. 아이디어 :
    1) 브루트포스식의 백트래킹 문제다.
2. 시간복잡도 :
    1) O(N!) : N은 최대 10
3. 자료구조 :
    1)
'''


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

def dfs(start):
    if len(ans)==m:
        print(" ".join(map(str,ans)))

    for i in range(start, n+1):
        ans.append(i)
        dfs(i+1)
        ans.pop()
dfs(1)
