# https://www.acmicpc.net/problem/9934

'''
1. 아이디어 :
    1) dfs로 풀면 된다. 중간값을 루트로 하고, 왼쪽과 오른쪽을 나눠서 재귀적으로 탐색한다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''

import sys
input = sys.stdin.readline

levels = int(input())
nums = list(map(int, input().split()))
ans = [[] for x in range(levels)]
def dfs(nums_list, level):
    mid = len(nums_list) // 2
    if len(nums_list) == 1:
        ans[level-1].append(nums_list[0])
        return
    dfs(nums_list[:mid], level+1)
    dfs(nums_list[mid + 1:], level+1)
    ans[level-1].append(nums_list[mid])

dfs(nums,1)
for i in ans:
    print(*i)
