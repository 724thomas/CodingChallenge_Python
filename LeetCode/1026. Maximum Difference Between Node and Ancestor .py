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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def dfs(node, cmin, cmax):
            if not node:
                return

            ans[0] = max(ans[0], abs(cmax-node.val), abs(cmin-node.val))

            cmin = min(node.val,cmin)
            cmax = max(node.val,cmax)

            dfs(node.left, cmin, cmax)
            dfs(node.right, cmin, cmax)

        dfs(root,root.val,root.val)
        return ans[0]