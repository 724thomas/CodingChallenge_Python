# https://leetcode.com/problems/binary-tree-pruning/description/

'''
1. 아이디어 :
    dfs를 이용해서, 노드의 왼쪽과 오른쪽을 구하고 노드의 값 + 왼쪽 + 오른쪽 = 0이면 None으로 바꾸면 된다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    트리
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if l==0:
                node.left = None

            if r==0:
                node.right = None
            return node.val + l + r

        return root if dfs(root) !=0 else None