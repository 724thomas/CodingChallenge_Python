# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

'''
1. 아이디어 :
    1) bfs로 해당 노드 레벨을 탐색한다.
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        deq = deque([root])

        while deq:
            deqlen = len(deq)
            templist = []
            for i in range(deqlen):
                temp = deq.popleft()
                if temp.left:
                    deq.append(temp.left)
                    templist.append(temp.left.val)
                if temp.right:
                    deq.append(temp.right)
                    templist.append(temp.right.val)
            if templist:
                ans.append(templist)
        return ans





