# https://www.acmicpc.net/problem/14248

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque
def solution(n, arr, start):
    visited = set()

    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        curr = queue.popleft()

        for i in range(-arr[curr], arr[curr]):
            target = curr + i
            if 0<= target < len(arr) and target not in visited:
                visited.add(target)
                queue.append(target)
    return len(visited)

n = int(input())
arr = list(map(int, input().split()))
start = int(input().strip()) - 1
print(solution(n, arr, start))


