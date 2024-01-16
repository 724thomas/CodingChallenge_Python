# https://www.acmicpc.net/problem/1697 숨바꼭질

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''
import sys
from collections import deque, defaultdict

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
queue = deque()
queue.append(n)
visited = defaultdict(int)
while queue:
    start = queue.popleft()
    if start == m:
        print(visited[start])
        exit()

    for cnext in (start - 1, start + 1, start * 2):
        if 0 <= cnext <= 100001 and cnext not in visited:
            visited[cnext] = visited[start]+1
            queue.append(cnext)
