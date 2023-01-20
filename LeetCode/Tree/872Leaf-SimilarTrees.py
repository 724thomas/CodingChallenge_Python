#https://leetcode.com/problems/leaf-similar-trees/description/

'''
1. 아이디어 :
    1) dfs로 풀기.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) dfs
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def dfs(node,nums):
            if node:
                if node.left==None and node.right==None:
                    nums.append(node.val)
                if node.left:
                    dfs(node.left,nums)
                if node.right:
                    dfs(node.right, nums)
            return nums

        return dfs(root1,[]) == dfs(root2,[])



