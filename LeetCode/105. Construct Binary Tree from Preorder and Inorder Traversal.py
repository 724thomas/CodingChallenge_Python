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
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        in_idx = defaultdict(int)
        for i, n in enumerate(inorder):
            in_idx[n] = i

        def dfs(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e or in_s > in_e:
                return None

            mid = preorder[pre_s]
            mid_idx = in_idx[mid]

            left_size = mid_idx - in_s

            node = TreeNode(mid)
            node.left = dfs(pre_s + 1, pre_s + left_size, in_s, mid_idx-1)
            node.right = dfs(pre_s + left_size + 1, pre_e, mid_idx+1, in_e)
            return node

        return dfs(0, len(preorder)-1, 0, len(inorder)-1)
