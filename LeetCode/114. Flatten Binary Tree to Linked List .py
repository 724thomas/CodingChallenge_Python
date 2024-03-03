#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def find_leaf(node):
            curr = node
            while curr.right:
                curr = curr.right
            return curr

        def dfs(node):
            if not node:
                return

            if node.left and node.right:
                cleft = dfs(node.left)
                left_end = find_leaf(cleft)
                left_end.right = dfs(node.right)
                node.right = cleft

            elif node.left:
                node.right = dfs(node.left)

            elif node.right:
                node.right = dfs(node.right)

            node.left = None
            return node

        return dfs(root)

