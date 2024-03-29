#https://leetcode.com/problems/clone-graph/description/

'''
1. 아이디어 :
    oldToNew 해시맵을 만들고, 기존 노드와 새로운 노드를 맵핑한다.
2. 시간복잡도 :
    O(v+e)
    nodes + edges
3. 자료구조 :
    해시맵, 배열
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node]=copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None