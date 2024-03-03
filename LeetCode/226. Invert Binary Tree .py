#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return root