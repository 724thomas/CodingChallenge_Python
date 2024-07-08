#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            if x!= par[x]:
                par[x] = find(par[x])
            return par[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return False
            if rank[ra] > rank[rb]:
                par[rb] = ra
            elif rank[ra] < rank[rb]:
                par[ra] = rb
            else:
                par[rb] = ra
                rank[ra] +=1
            return True

        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        for a, b in edges:
            if union(a,b):
                n -= 1
        return n


