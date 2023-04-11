#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return
        clone=Node(root.val,[])

        def dfs(node,cnode):
            if not node:
                return
            print(node.val)
            for c in node.children:
                cchild=Node(c.val,[])
                cnode.children.append(cchild)
                dfs(c,cchild)


        dfs(root,clone)
        return clone