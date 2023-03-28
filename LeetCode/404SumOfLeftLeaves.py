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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=[]

        def dfs(node, lr):
            if not node:
                return

            if not node.left and not node.right and lr=="l":
                ans.append(node.val)
            dfs(node.left,"l")
            dfs(node.right,"r")

        dfs(root,"r")

        return sum(ans)