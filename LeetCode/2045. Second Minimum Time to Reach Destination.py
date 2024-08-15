#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque, defaultdict
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([1])
        cur_time = 0
        found = False
        visit_times = defaultdict(list)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if found:
                        return cur_time
                    found = not found
                for nei in graph[node]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        nei_times.append(cur_time)

            if (cur_time // change) % 2==1:
                cur_time += change - (cur_time % change)
            cur_time += time