#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque, defaultdict
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        candids = defaultdict(list)
        graph = defaultdict(list)

        for i in range(len(original)):
            graph[original[i]].append([changed[i], cost[i]])

        def bfs(char):
            candid_cost = defaultdict(int)
            visited = set()
            visited.add(char)
            queue = deque()
            queue.append((char, 0))

            while queue:
                curr, cost = queue.popleft()

                for nxt, cost2 in graph[curr]:
                    if nxt in candid_cost and cost+cost2 > candid_cost[nxt]:
                        continue
                    visited.add(nxt)
                    candid_cost[nxt] = cost+cost2
                    queue.append((nxt, cost+cost2))
            return candid_cost

        for i in range(26):
            candids[chr(97+i)] = bfs(chr(97+i))

        ans = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            candid = candids[source[i]]
            if target[i] not in candid:
                return -1
            ans += candid[target[i]]
        return ans