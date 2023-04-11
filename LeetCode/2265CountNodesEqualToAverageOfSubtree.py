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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def dfs(node):
            if not node:
                return [0,0]
            l=dfs(node.left)
            r=dfs(node.right)
            total=node.val+l[0]+r[0]
            count=1+l[1]+r[1]
            if int(total/count)==node.val:

                self.ans+=1
            return [total,count]

        dfs(root)
        return self.ans

