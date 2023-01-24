#https://leetcode.com/problems/binary-tree-maximum-path-sum/

'''
1. 아이디어 :
    1) DFS로 풀 수 있다. 각 노드마다, 왼쪽자식, 오른쪽 자식의 max를 구한다.
    각 노드의 최대값(한쪽으로 내려갈때)를 리턴한다.
        max경우의 수
        a) 왼쪽, 본인, 오른쪽을 합친게 제일 크다.
        b) 위 노드를 타고 내려온 후, 왼쪽 오른쪽 합친게 제일 크다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) Binary Tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            lMax = dfs(node.left)
            rMax = dfs(node.right)
            lMax = max(lMax,0)
            rMax = max(rMax,0)
            ans = max(ans, node.val + lMax + rMax)
            print(node.val, lMax, rMax, ans)
            return node.val + max(lMax, rMax)


        dfs(root)
        return ans




