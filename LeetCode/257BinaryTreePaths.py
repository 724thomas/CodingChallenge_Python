# https://leetcode.com/problems/binary-tree-paths/description/

'''
1. 아이디어 :
    1)  dfs로 풀 수 있다. 노드를 순회하며 경로를 저장하고, leaf 노드에 도달하면 경로를 ans 배열에 저장한다.
    2)  bfs(iterationo)로도 풀 수 있다. ans, stack 배열을 만들고, leaf를 도착하면 ans에 경로를 저장하고, 그렇지 않으면
        stack에 "->"+ 경로를 저장한다.
2. 시간복잡도 :
    1)  O(n)
    -   탐색 시간
    2)  O(n)
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, path):
            if not node:
                return

            path +="->"+ str(node.val)

            if not node.right and not node.left:
                ans.append(path[2:])
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return ans

2)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        ans = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val))) \
        return ans