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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dict = defaultdict(int)
        dict[0] = 1


        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                count = dict[total-targetSum]

                dict[total] += 1
                count += dfs(root.left, total) + dfs(root.right, total)
                dict[total] -= 1

            return count

        return dfs(root, 0)
