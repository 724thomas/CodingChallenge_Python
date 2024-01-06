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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]

        def dfs(node, nums):
            nums.append(str(node.val))
            if not node.left and not node.right:
                ans.append(int("".join(nums)))

            if node.left:
                dfs(node.left, nums)

            if node.right:
                dfs(node.right, nums)
            nums.pop()

        dfs(root, [])
        return sum(ans)