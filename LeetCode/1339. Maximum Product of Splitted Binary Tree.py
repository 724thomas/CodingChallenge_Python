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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.totals = []
        def getTotal(node):
            if not node:
                return 0

            self.total+=node.val

            curr = node.val + getTotal(node.left) + getTotal(node.right)
            self.totals.append(curr)
            return curr

        getTotal(root)

        ans = 0
        for n in self.totals:
            ans = max(ans, (self.total-n) * n)
        return ans % (10**9 + 7)