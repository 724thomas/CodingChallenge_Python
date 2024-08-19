#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
import heapq
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        erased = defaultdict(int)
        for i, t in enumerate(disappear):
            erased[i]=t

        min_heap = [[0,0]] #time, start
        visited = set()
        ans = [-1] * n

        while min_heap:
            total, curr = heapq.heappop(min_heap)
            if curr in visited:
                continue
            visited.add(curr)
            ans[curr] = total

            for neighbor, time in graph[curr]:
                if total + time >= erased[neighbor] or neighbor in visited:
                    continue
                heapq.heappush(min_heap, (total+time, neighbor))

        return ans



