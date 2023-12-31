# https://school.programmers.co.kr/learn/courses/30/lessons/86971 전력망을 둘로 나누기

'''
1. 아이디어 :
    해당 node의 사이즈를 구하는 dfs를 만든다.
    연결되는 graph를 만들고, wire를 하나씩 끊어보면서 n - 2*노드사이즈를 구한다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    해시맵
'''

from collections import defaultdict

def dfs(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size += dfs(graph, neighbor, visited)
    return size

def solution(n, wires):

    graph = defaultdict(set)
    for start, end in wires:
        graph[start].add(end)
        graph[end].add(start)

    min_diff = n

    for start, end in wires:
        graph[start].remove(end)
        graph[end].remove(start)

        visited = set()
        subgraph_size = dfs(graph, start, visited)

        diff = abs(n - 2 * subgraph_size)
        min_diff = min(min_diff, diff)

        graph[start].add(end)
        graph[end].add(start)

    return min_diff
