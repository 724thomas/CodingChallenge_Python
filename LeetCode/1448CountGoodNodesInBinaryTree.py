# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

'''
1. 아이디어 :
    1) dfs로 탐색하면서, 노드가 없으면 0, 노드의 값이 value보다 크거나 같으면 ans+=1. maxvalue를 현재 노드와 비교하여 갱신하고,
    자식 노드들도 dfs로 실행한다.
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
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node, value):
            nonlocal ans
            if not node:
                return 0
            if node.val >= value:
                ans+=1
            maxval = max(value,node.val)
            dfs(node.left,maxval)
            dfs(node.right,maxval)

        dfs(root,-float('inf'))
        return ans

