#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dict = defaultdict(int)

        def dfs(node, level):
            if not node:
                return

            dict[level] = node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)
        return [dict[i] for i in range(len(dict))]
