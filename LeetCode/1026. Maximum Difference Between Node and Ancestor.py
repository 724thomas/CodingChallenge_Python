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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def dfs(node, cmax, cmin):
            if not node:
                return
            self.ans=max(self.ans, abs(cmax-node.val), abs(cmin-node.val))
            cmax=max(node.val,cmax)
            cmin=min(node.val,cmin)
            dfs(node.left, cmax, cmin)
            dfs(node.right, cmax, cmin)
        dfs(root,root.val,root.val)
        return self.ans