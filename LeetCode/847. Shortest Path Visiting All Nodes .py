#https://leetcode.com/problems/shortest-path-visiting-all-nodes/

'''
1. 아이디어 :
    bfs로 풀어야하지만 dfs로 시도했다. - 시간초과
2. 시간복잡도 :
    O(N^2) + O(N^2)
3. 자료구조 :
    그래프, 배열
'''

class Solution:
    def shortestPathLength(self, g: List[List[int]]) -> int:
        if len(g)==0:
            return 0
        if len(g[0])==0:
            return 0

        #Construct Graph
        graph = {}
        for i in range(len(g)):
            for j in range(len(g[i])):
                if i!=j:
                    if i not in graph:
                        graph[i]=set()
                    graph[i].add(g[i][j])
                    if g[i][j] not in graph:
                        graph[g[i][j]] = set()
                    graph[g[i][j]].add(i)

        #dfs search to find min path from A to B
        def min_path(start, dest, node, length):
            # print(start,dest,node,length)
            if length>self.cmax:
                return

            if node == dest:
                self.cmax = min(self.cmax, length)

            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    min_path(start, dest, n, length+1)
                    visited.remove(n)

        # 2D dp for min path from A to B
        dp = [[1] * len(g) for x in range(len(g))]
        for i in range(len(dp)):
            for j in range(i, len(dp)):
                visited = set()
                visited.add(i)
                self.cmax = 12**2
                min_path(i,j,i,0)
                dp[i][j] = self.cmax
                dp[j][i] = self.cmax


        def dfs(node, length):
            if len(visited) == len(g):
                self.cmax = min(self.cmax, length)
                return

            for i in range(len(dp)):
                if i not in visited:
                    visited.append(i)
                    dfs(i, length+dp[node][i])
                    visited.pop()

        ans = float('inf')
        for i in range(len(g)):
            self.cmax = float('inf')
            visited = []
            dfs(i,0)
            ans = min(ans, self.cmax)

        return ans