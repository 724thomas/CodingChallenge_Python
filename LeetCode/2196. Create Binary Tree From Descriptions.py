#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        visited = set()
        nodes = {}
        for par, chi, is_left in descriptions:
            visited.add(chi)
            if par in nodes:
                parent = nodes[par]
            else:
                parent = TreeNode(par)
                nodes[par] = parent
            if chi in nodes:
                child = nodes[chi]
            else:
                child = TreeNode(chi)
                nodes[chi] = child

            if is_left:
                parent.left = child
            else:
                parent.right = child

        for par, chi, is_left in descriptions:
            if par not in visited:
                return nodes[par]