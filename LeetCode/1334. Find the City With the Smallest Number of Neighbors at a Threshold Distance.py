#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distances[i][i] = 0
        for u, v, d in edges:
            distances[u][v] = d
            distances[v][u] = d

        for mid in range(n):
            for start in range(n):
                for end in range(n):
                    if distances[start][end] > distances[start][mid] + distances[mid][end]:
                        distances[start][end] = distances[start][mid] + distances[mid][end]

        cities = float('inf')
        city = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if i==j:
                    continue
                elif distances[i][j] <= distanceThreshold:
                    count+=1
            if count <= cities:
                cities = count
                city = i
        return city