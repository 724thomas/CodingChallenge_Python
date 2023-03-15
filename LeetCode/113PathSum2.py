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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]

        def dfs(node, total, path):
            path.append(node.val)
            if not node.left and not node.right:
                if total+node.val==targetSum:
                    ans.append(path.copy())

            if node.left:
                dfs(node.left, total+node.val, path)

            if node.right:
                dfs(node.right, total+node.val, path)
            path.pop()

        if root:
            dfs(root, 0, [])
        return ans
