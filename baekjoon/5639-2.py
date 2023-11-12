# https://www.acmicpc.net/problem/5639

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

import sys
sys.setrecursionlimit(10**9)

nodes = []
while True:
    try:
        nodes.append(int(sys.stdin.readline()))
    except:
        break

def dfs(arr):
    if not arr:
        return

    front = arr[0]
    mid = 1

    while mid <= len(arr)-1 and arr[mid]<=front:
        mid+=1

    dfs(arr[1:mid])
    dfs(arr[mid:])
    print(front)

dfs(nodes)



