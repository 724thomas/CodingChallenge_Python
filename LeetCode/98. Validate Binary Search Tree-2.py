#

'''
1. 아이디어 :
    left와 right 범위를 사이를 확인한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, node, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return dfs(left, node.left, node.val) and dfs(node.val, node.right, right)

        return dfs(-float('inf'), root, float('inf'))


