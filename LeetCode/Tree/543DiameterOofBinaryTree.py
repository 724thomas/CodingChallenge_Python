# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    1) DFS로 풀 수 있다. 각 노드의 차일드의 height를 저장하고, 해당 노드는 두 차일드 +1개의 height이고,
    최대 길이는 두 차일드의 height +2 가된다. max를 이용하여 최대값 갱신한다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) DFS
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter=[0]

        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            maxDiameter[0] = max(maxDiameter[0], 2+left+right)

            height = 1 + max(left,right)
            return height

        dfs(root)
        return maxDiameter[0]