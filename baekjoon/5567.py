# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import deque, defaultdict


def solution(n, m, arr):
    graph = defaultdict(list)
    for u, v in arr:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    queue.append([1,0])
    visited = set()
    visited.add(1)
    count = 0
    while queue:
        curr, depth = queue.popleft()
        if depth >= 2:
            continue
        for friend in graph[curr]:
            if friend in visited:
                continue
            visited.add(friend)
            queue.append((friend, depth + 1))
            count += 1

    return count


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, m, arr))
