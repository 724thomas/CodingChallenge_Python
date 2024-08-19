#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = graph
        safe = {}

        def dfs(curr):
            if curr in safe:
                return safe[curr]

            safe[curr] = False

            for neighbor in graph[curr]:
                if not dfs(neighbor):
                    return False
            safe[curr] = True
            return True

        for i in range(len(graph)):
            dfs(i)
        return sorted([k for k, v in safe.items() if v == True])

