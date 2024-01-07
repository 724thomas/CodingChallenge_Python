# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            parent = queue.popleft()

            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)
                parent.left.next = parent.right
                if parent.next:
                    parent.right.next = parent.next.left
        return root
