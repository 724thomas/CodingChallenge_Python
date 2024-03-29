# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

'''
1. 아이디어 :
    inorder traversal을 하면서 k번째 원소를 찾으면 된다.
2. 시간복잡도 :
    O(N)
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []

        def inorder(node):
            if not node or len(inorder_list) >= k:
                return

            inorder(node.left)
            inorder_list.append(node.val)
            inorder(node.right)

        inorder(root)
        return inorder_list[k-1]