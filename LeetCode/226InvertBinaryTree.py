# https://leetcode.com/problems/invert-binary-tree/description/

'''
1. 아이디어 :
    1) dfs로 풀 수 있다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) DFS
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                node.left, node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return root