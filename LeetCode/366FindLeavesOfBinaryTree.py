#https://leetcode.com/problems/find-leaves-of-binary-tree/

'''
1. 아이디어 :
    재귀를 이용하여 풀 수 있다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    리스트
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]

        def dfs(node):
            if not node:
                return False
            if not node.left and not node.right:

                temp.append(node.val)
                return True

            if dfs(node.left):
                node.left=None
            if dfs(node.right):
                node.right=None

        temp=[]
        while root.left or root.right:
            temp=[]
            dfs(root)
            ans.append(temp.copy())
        ans.append([root.val])
        return ans
