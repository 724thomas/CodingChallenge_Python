#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = [0]

        def dfs(node, level):
            if not node:
                return []

            if not node.left and not node.right: #if leaf
                return [level]

            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)

            for left_leaf in left:
                for right_leaf in right:
                    if (left_leaf-level) + (right_leaf-level) <= distance:
                        ans[0] += 1

            return left + right

        dfs(root, 0)
        return ans[0]



