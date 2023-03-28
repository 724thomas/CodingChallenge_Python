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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans=[]

        def dfs(node):
            if not node:
                return
            if node.val not in ans:
                ans.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        ans.sort()

        return ans[1] if len(ans)>=2 else -1