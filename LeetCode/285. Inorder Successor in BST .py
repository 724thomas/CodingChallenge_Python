# https://leetcode.com/problems/inorder-successor-in-bst/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        ans = []

        def dfs(node):
            if not node:
                return

            if node.val > p.val:
                ans.append([node.val,node])
                dfs(node.left)
            else:
                dfs(node.right)

        dfs(root)
        ans.sort()
        return ans[0][1] if ans else None

