# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

'''
1. 아이디어 :
    dfs를 활용한다. total 값을 두고,
    dfs(node.right)을 통해 오른쪽의 값을 total에 추가 한후, node.val에 total 값을 넣어준다.
    dfs(node.left)를 통해 왼쪽 값은 마지막에 넣는다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    이진트리
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):
        self.total = 0

        def dfs(node):
            if not node:
                return

            dfs(node.right)
            self.total +=  node.val
            node.val=self.total
            dfs(node.left)

        dfs(root)
        return root