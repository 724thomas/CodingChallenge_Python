#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

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
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_index = defaultdict(int)
        for idx, num in enumerate(inorder):
            inorder_index[num] = idx

        def dfs(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start > preorder_end or inorder_start > inorder_end:
                return None

            parent = preorder[preorder_start]
            parent_index = inorder_index[parent]

            left_tree_size = parent_index - inorder_start

            root = TreeNode(parent)
            root.left = dfs(preorder_start + 1, preorder_start + left_tree_size, inorder_start, parent_index - 1)
            root.right = dfs(preorder_start + left_tree_size + 1, preorder_end, parent_index + 1, inorder_end)

            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)