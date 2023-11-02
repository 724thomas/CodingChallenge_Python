#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

k = int(input())
nodes = list(map(int,input().split()))
ans = {}
def dfs(k, arr):
    if not arr:
        return
    mid = len(arr)//2

    if k not in ans:
        ans[k] = []
    ans[k].append(str(arr[mid]))

    dfs(k+1, arr[:mid])
    dfs(k+1, arr[mid+1:])

dfs(0, nodes)
for n in ans:
    print(" ".join(ans[n]))