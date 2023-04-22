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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans=0

        def dfs(node, gp, p):
            if not node:
                return

            if gp:
                self.ans+=node.val
            iseven=node.val%2==0
            dfs(node.left, p, iseven)
            dfs(node.right, p, iseven)
        dfs(root,False,False)

        return self.ans

