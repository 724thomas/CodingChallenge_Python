# https://leetcode.com/problems/find-center-of-star-graph/description/

'''
1. 아이디어 :
    1) paths 해시맵에 모든 경로를 다 저장한다. 경로 중에 가장 많이 나온 노드가 답이다.
    2) 하나의 노드는 항상 모든 edges에 존재하므로, edges[0][0]과 edges[0][1] 중에 하나가 답이다.
2. 시간복잡도 :
    O(N) * O(1)
    해시맵 저장 * 해시맵 접근
    O(1)
    edges[0][0] or edges[0][1]
3. 자료구조 :
    1) 해시맵
    2) 배열
'''

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        paths = {}
        for e in edges:
            s=e[0]
            d=e[1]
            if s not in paths:
                paths[s] = [d]
            else:
                paths[s].append(d)
            if d not in paths:
                paths[d] = [s]
            else:
                paths[d].append(s)

        for k, v in paths.items():
            if len(v)==len(edges):
                return k



class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
