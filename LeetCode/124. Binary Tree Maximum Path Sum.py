#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        cmax = [root.val]
        print(cmax[0])

        def dfs(node):
            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            cmax[0] = max(cmax[0], left + node.val + right)
            return max(0, left+node.val, right+node.val)

        dfs(root)
        return cmax[0]