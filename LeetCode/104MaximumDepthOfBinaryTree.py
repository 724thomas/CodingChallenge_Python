#https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            else:
                return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)