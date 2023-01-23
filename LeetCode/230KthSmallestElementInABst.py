#

'''
1. 아이디어 :
    1) BFS, DFS로 풀 수 있지만, BFS로 스택을 만들고, 왼쪽이 아닌 오른쪽부터 빼게되면, 순서대로 빠지기 때문에
    BST에서 쓰기 좋다.
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

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left

            cur = stack.pop()
            print(cur.val)
            n+=1
            if n==k:
                return cur.val
            cur = cur.right
