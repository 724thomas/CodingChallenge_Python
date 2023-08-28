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
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count=0

        def dfs(node):
            if not node:
                return set()

            lset=dfs(node.left)
            rset=dfs(node.right)
            if len(lset)==1:
                self.count+=1
            if len(rset)==1:
                self.count+=1

            nset=(lset|rset)
            nset.add(node.val)
            return nset

        if len(dfs(root))==1:
            self.count+=1
        return self.count