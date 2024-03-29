#https://leetcode.com/problems/same-tree/

'''
1. 아이디어 :
    1) DFS로 풀 수 있다
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return dfs(node1.left,node2.left) and dfs(node1.right, node2.right)
        return dfs(p,q)

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return True

        deq = deque([(p,q)])
        print(deq)
        while deq:
            p, q = deq.popleft()
            if not check(p,q):
                return False

            if p:
                deq.append((p.left,q.left))
                deq.append((p.right,q.right))

        return True
