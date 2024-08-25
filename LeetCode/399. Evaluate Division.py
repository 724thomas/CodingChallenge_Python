#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            a, b = equations[i]
            val = values[i]
            graph[a].append((b, 1/val))
            graph[b].append((a, val))
        print(graph)

        def bfs(start, end):
            visited = set()
            visited.add(start)
            queue = deque()
            queue.append((start, 1))

            while queue:
                curr, val = queue.popleft()
                if curr == end:
                    return val

                for neighbor, val2 in graph[curr]:
                    if neighbor in visited: continue
                    visited.add(neighbor)
                    queue.append((neighbor, val / val2))

            return -1
        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1)
            else:
                ans.append(bfs(a,b))
        return ans