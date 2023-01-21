#https://leetcode.com/problems/subtree-of-another-tree/

'''
1. 아이디어 :
    1) DFS
2. 시간복잡도 :
    1) O(n) * O(n) = O(n^2)
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node,subnode):
            if not subnode:
                return True
            if not node:
                return False

            if check(node, subnode):
                return True
            return dfs(node.left, subnode) or dfs(node.right, subnode)

        def check(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val==node2.val:
                return check(node1.left, node2.left) and check(node1.right, node2.right)
            return False

        return dfs(root,subRoot)
