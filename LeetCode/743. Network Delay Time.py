#

'''
1. 아이디어 :
    다익스트라
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''


import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        distance = [[0] * (n + 1) for _ in range(n + 1)]
        dict = defaultdict(list)

        for start, dest, dist in times:
            distance[start][dest] = dist
            dict[start].append(dest)

        min_heap = [(0,k)]
        ans = 0

        while min_heap:
            total, curr = heapq.heappop(min_heap)
            if curr in visited:
                continue
            visited.add(curr)

            ans = max(ans, total)

            for neighbor in dict[curr]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (total+distance[curr][neighbor], neighbor) )

        return ans if len(visited) == n else -1



