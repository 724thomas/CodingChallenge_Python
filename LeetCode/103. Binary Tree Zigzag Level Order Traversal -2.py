# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = defaultdict(list)
        max_depth = [0]

        def dfs(node, depth):
            if not node:
                return

            hmap[depth].append(node.val)
            max_depth[0] = max(max_depth[0], depth)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)
        ans = []
        for i in range(max_depth[0]):
            if i%2==0:
                ans.append(hmap[i+1])
            else:
                ans.append(hmap[i+1][::-1])
        return ans