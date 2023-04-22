#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        sums={}
        self.cmax=0

        def dfs(node, depth):
            if not node:
                self.cmax=max(self.cmax,depth-1)
                return
            if depth not in sums:
                sums[depth]=node.val
            else:
                sums[depth]+=node.val

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)
        return sums[self.cmax]
        print(sums, self.cmax)
