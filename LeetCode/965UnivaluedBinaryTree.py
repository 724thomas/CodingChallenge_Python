#https://leetcode.com/problems/univalued-binary-tree/description/

'''
1. 아이디어 :
    1)  dfs로 풀 수 있다. 노드가 있으면 값을 root값과 비교하고, 노드가 있으면 True 틀리면 False를 호출.
        왼쪽, 오른쪽 노드를 재귀 호출한다.
    2)  bfs로 풀 수 있다. stack에 root를 추가하고, stack이 비어있지 않으면, node를 stack에서 pop한다.
2. 시간복잡도 :
    1)   O(n)
    -   탐색 시간
    2)   O(n)
    -   탐색 시간
3. 자료구조 :
    1)  Binary Tree
    2)  Binary Tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#1)
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        base = [root.val]
        def dfs(node):
            if not node:
                return True
            if node.val!=base[0]:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)

#2)
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        base =root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != base:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
