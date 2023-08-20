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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def dfs(node, level):
            if not node:
                return

            if len(ans)<level:
                ans.append(node.val)
            else:
                ans[level-1]+=node.val

            dfs(node.left,level+1)
            dfs(node.right,level+1)

        dfs(root, 1)
        ans.sort(reverse=True)
        return ans[k-1] if len(ans)>=k else -1