# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    1) BFS로 풀기.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) BFS
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def bfs(node):
            nonlocal ans
            if node:
                if low<=node.val<=high:
                    ans+=node.val
                if low<node.val:
                    bfs(node.left)
                if node.val<high:
                    bfs(node.right)


        ans = 0
        bfs(root)
        return ans
