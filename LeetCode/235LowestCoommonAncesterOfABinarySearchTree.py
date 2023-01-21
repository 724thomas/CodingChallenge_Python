#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

'''
1. 아이디어 :
    1) while문으로 노드를 하나씩 내려가면서, p, q가 해당 노드보다 값이 작으면 노드를 왼쪽으로, 반대면 오른쪽으로 가고,
    둘다 아니면 양쪽으로 가기때문에 해당 노드를 리턴하면 된다.
2. 시간복잡도 :
    1) O(logn)
3. 자료구조 :
    1) 이진트리
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr