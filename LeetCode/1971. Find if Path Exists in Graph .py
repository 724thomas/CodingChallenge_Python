# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

'''
1. 아이디어 :
    dfs를 이용해서 풀 수 있다. 해시맵에 노드와 노드와 연결된 노드들을 저장하고,,
    dfs를 이용하여 source에서 destination까지 도달할 수 있는지 확인한다.
2. 시간복잡도 :
    O(N) * O(1)
    방문 노드 수 * 해시맵 접근
3. 자료구조 :
    해시맵, 해시셋
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.ans = False
        visited = set()

        paths = {}
        for e in edges:
            s=e[0]
            d=e[1]
            if s not in paths:
                paths[s]=[d]
            else:
                paths[s].append(d)
            if d not in paths:
                paths[d]=[s]
            else:
                paths[d].append(s)

        def dfs(node=source):
            if node in visited:
                return
            visited.add(node)
            if destination in paths[node]:
                self.ans=True
                return

            for n in paths[node]:
                dfs(n)

        if source==destination:
            return True
        dfs()
        return self.ans
