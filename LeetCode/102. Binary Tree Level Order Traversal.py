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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node,level):
            if not node:
                return
            if len(ans)<level:
                ans.append([])
            ans[level-1].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)


        dfs(root, 1)
        return ans