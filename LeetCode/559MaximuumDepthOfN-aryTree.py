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
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans=1
        if not root:
            return 0

        def dfs(node, depth):
            self.ans=max(self.ans, depth)

            for c in node.children:
                dfs(c, depth+1)

        dfs(root,1)
        return self.ans