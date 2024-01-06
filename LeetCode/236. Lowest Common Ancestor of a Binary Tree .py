# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

'''
1. 아이디어 :
    dfs로 가다가 아래에 p나 q가 있으면, left와 right에 p또는 q로 바꿔서 확인한다
2. 시간복잡도 :
    o(n)
3. 자료구조 :
    트리
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def check(node, p, q):
            if not node or node == p or node == q:
                return node

            left = check(node.left, p, q)
            right = check(node.right, p, q)
            if left and right:
                return node

            return left if left else right


        return check(root,p,q)