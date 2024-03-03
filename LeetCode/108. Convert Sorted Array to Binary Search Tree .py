#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(left, right):
            if right-left+1 >=3:
                mid = (right+left)//2
                par = TreeNode(nums[mid])
                par.left = dfs(left, mid-1)
                par.right = dfs(mid+1, right)

            elif right-left==1:
                par = TreeNode(nums[left])
                par.right = TreeNode(nums[right])

            else:
                par = TreeNode(nums[left])

            return par


        return dfs(0, len(nums)-1) if len(nums)>=2 else TreeNode(nums[0])
