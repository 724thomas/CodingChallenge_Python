# https://www.acmicpc.net/problem/1766

'''
1. 아이디어 :
    heapq를 통해서 쉬운 문제들중에 idx가 우선인 애들을 정렬
    defaultdict를 통해 토폴로지를 생성
    in_degree 배열을 통해, 선행 문제들의 카운트를 저장
2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    해시맵
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
import heapq
def solution(N, edges):
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)

    # 그래프 구성 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # 진입 차수가 0인 노드를 우선순위 큐에 추가
    min_heap = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            heapq.heappush(min_heap, i)

    result = []

    # 우선순위 큐를 이용한 위상 정렬
    while min_heap:
        node = heapq.heappop(min_heap)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(min_heap, neighbor)

    return result




n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
sorted_problems = solution(n, edges)
print(" ".join(map(str, sorted_problems)))

