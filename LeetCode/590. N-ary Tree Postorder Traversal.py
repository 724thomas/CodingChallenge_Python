#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
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
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def post(node):
            if not node:
                return

            for child in node.children:
                post(child)
            ans.append(node.val)
        if not root:
            return []
        post(root)
        return ans