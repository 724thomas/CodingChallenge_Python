# https://leetcode.com/problems/count-complete-tree-nodes/description/

'''
1. 아이디어 :
    1)  dfs로 풀 수 있다. 노드가 있으면 ans 배열에 1추가하며 재귀를 호출한다.
    2)  bfs로 풀 수 있다. ans=0, stack =[]을 선언 후, ans+=1, stack에 left, right를 추가한다.
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

1)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(1)
        dfs(root)
        return sum(ans)


2)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            ans+=1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ans