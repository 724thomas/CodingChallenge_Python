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
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.curr = 1
        self.ans = -1

        def dfs(node):

            if not node:
                return
            print(self.curr, node.val)
            if self.ans!=-1:
                return

            dfs(node.left)
            self.curr+=1
            if self.curr == k:
                ans = node.val
            dfs(node.right)

        dfs(root)
        return self.ans

