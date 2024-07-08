#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(a,b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return True

            if rank[ra] > rank[rb]:
                par[rb] = ra
            elif rank[ra] < rank[rb]:
                par[ra] = rb
            else:
                par[rb] = ra
                rank[ra] += 1
            return False

        par = [i for i in range(n)]
        rank = [1 for i in range(n)]

        for a, b in edges:
            if union(a,b):
                return False

        base = find(par[0])
        for i in range(1, len(par)):
            if find(i) != base:
                return False


        return True