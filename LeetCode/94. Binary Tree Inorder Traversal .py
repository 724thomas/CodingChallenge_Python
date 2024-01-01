# https://leetcode.com/problems/binary-tree-inorder-traversal/

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(node):
            if not node:
                return

            ans.append(node.val)
            inorder(node.left)
            inorder(node.right)

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        def postorder(node):
            if not node:
                return

            inorder(node.left)
            inorder(node.right)
            ans.append(node.val)

        inorder(root)
        return ans
