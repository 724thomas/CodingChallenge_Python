# https://www.acmicpc.net/problem/15657

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
ans = []

def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return

    for i in range(start, n):
        ans.append(nums[i])
        dfs(i)
        ans.pop()
dfs(0)

