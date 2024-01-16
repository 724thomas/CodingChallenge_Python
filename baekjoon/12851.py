# https://www.acmicpc.net/problem/12851 숨바꼭질2

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
fastest = float('inf')
count = 0
while queue:
    start = queue.popleft()
    if start == m:
        fastest = visited[start]
        count+=1
        continue

    for cnext in (start - 1, start + 1, start * 2):
        if 0 <= cnext <= 100001 and (cnext not in visited or visited[cnext] == visited[start] + 1):
            visited[cnext] = visited[start]+1
            queue.append(cnext)

print(fastest)
print(count)