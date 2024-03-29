# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    1) dfs를 이용해서, 양쪽 노드의 값을 비교한다.
    2) bfs를 이용할 수 있다.
2. 시간복잡도 :
    1) O(n)
    2) bfs의 경우, O(n)
3. 자료구조 :
    1) tree
    2) queue

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(lnode, rnode):
            if not lnode and not rnode:
                return True
            if not lnode or not rnode:
                return False
            if lnode.val != rnode.val:
                return False
            return dfs(lnode.left, rnode.right) and dfs(lnode.right, rnode.left)

        return dfs(root.left,root.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            lnode, rnode = queue.pop(0)
            if lnode and rnode:
                if lnode.val == rnode.val:
                    queue.append((lnode.left, rnode.right))
                    queue.append((lnode.right, rnode.left))
                else:
                    return False
            elif (lnode and rnode==None) or (lnode==None and rnode):
                return False
        return True