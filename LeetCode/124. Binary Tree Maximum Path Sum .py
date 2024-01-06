# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

'''
1. 아이디어 :
    dfs를 사용한다.
    자식들중 0보다 작을경우에는 방문하지 않으므로 max(0, 자식)으로 갱신한다
    ans를 왼쪽+오른쪽+본인으로 갱신하고,
    max(왼쪽, 오른쪽) + 본인을 위로 리턴한다.
2. 시간복잡도 :
    o(n)
3. 자료구조 :
    트리
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            ans[0] = max(ans[0], left+right+node.val)
            return max(left, right) + node.val

        ans = [-float('inf')]
        dfs(root)
        return ans[0]

