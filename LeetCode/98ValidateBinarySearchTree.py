# https://leetcode.com/problems/validate-binary-search-tree/description/

'''
1. 아이디어 :
    1) DFS로 풀 수 있다. 노드가 가질 수 있는 최소, 최대값을 갱신하면서, 해당 노드의 값을 확인한다
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 이진트리
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minval, maxval):
            if not node:
                return True
            if not(minval < node.val < maxval):
                return False
            return dfs(node.left, minval, node.val) and dfs(node.right, node.val, maxval)


        return dfs(root, -float('inf'), float('inf'))
