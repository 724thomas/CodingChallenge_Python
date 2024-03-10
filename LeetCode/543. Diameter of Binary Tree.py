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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0


            left = dfs(node.left)
            right = dfs(node.right)
            curr = left + right
            self.ans = max(self.ans, curr)

            return max(left,right)+1

        dfs(root)
        return self.ans
