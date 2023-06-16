# https://leetcode.com/problems/redundant-connection/

'''
1. 아이디어 :
    union find로 각 edge를 확인하면서, parent가 같을때는 필요 없는 edge이다.
2. 시간복잡도 :
    O(N^2)
    edges * find
3. 자료구조 :
    배열
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        par, rank = [], []
        for i in range(len(edges)+1):
            par.append(i)
            rank.append(1)

        def find(n1):
            res = par[n1]
            while res!=par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1==p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] +=1
            else:
                par[p1] = p2
                rank[p2] +=1
            return True

        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge



