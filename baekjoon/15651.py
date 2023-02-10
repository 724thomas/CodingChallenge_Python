# https://www.acmicpc.net/problem/15651

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


import sys
input = sys.stdin.readline
n, m = map(int,input().split())

ans = []
def backtracking():

    if len(ans) == m:
        print (' '.join(map(str,ans)))
        return
    for i in range(1, n+1):
        ans.append(i)
        backtracking()
        ans.pop()

backtracking()
