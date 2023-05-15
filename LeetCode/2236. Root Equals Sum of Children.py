# https://leetcode.com/problems/root-equals-sum-of-children/

'''
1. 아이디어 :
    root 값과 root의 왼쪽+오른쪽 값을 더한다.
2. 시간복잡도 :
    O(3)
3. 자료구조 :
    이진트리
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val