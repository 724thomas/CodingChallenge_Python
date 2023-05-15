# https://leetcode.com/problems/maximum-binary-tree/description/

'''
1. 아이디어 :
    dfs로 풀 수 있다.
    values (배열)을 매개변수로 받고, 배열의 제일 큰 값의 왼쪽을 left, 오른쪽을 right로 나누고,
    배열의 제일 큰 값은 new_node로 만든다.
    new_node의 왼쪽을 dfs(left), 오른쪽을 dfs(right)로 재귀적으로 만들고, 만들어진 new_node를 return 한다.
2. 시간복잡도 :
    O(N^2)
    value의 모든 값에 대한 처리 * value의 최대 값 탐색
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(values):
            if len(values)==0:
                return None

            max_index = values.index(max(values))
            new_node = TreeNode(values[max_index])

            left = values[:max_index]
            right = values[max_index+1:]

            new_node.left = dfs(left)
            new_node.right = dfs(right)
            return new_node

        return dfs(nums)



