# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k = [k]

        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            if left is not None:
                return left

            k[0]-=1
            if k[0] == 0:
                return node.val

            return dfs(node.right)

        return dfs(root)