#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = set()
        visited.add(0)
        ans = []
        path = [0]

        def backtrack(curr):
            if curr == len(graph)-1:
                ans.append(path.copy())

            for next_node in graph[curr]:
                if next_node not in visited:
                    visited.add(next_node)
                    path.append(next_node)
                    backtrack(next_node)
                    visited.remove(next_node)
                    path.pop()

        backtrack(0)
        return ans
