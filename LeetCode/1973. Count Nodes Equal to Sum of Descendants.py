#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.count=0

        def dfs(node):
            if not node:
                return 0
            add=dfs(node.left)+dfs(node.right)
            if node.val==add:
                self.count+=1

            return add+node.val

        dfs(root)
        return self.count