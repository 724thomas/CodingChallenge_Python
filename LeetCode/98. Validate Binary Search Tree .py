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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lv, rv):
            if not node:
                return True

            if not (lv<node.val<rv):
                return False

            return dfs(node.left, lv,node.val) and dfs(node.right,node.val, rv)

        return dfs(root, -float('inf'),float('inf'))


