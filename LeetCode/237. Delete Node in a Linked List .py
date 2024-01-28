# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

'''
1. 아이디어 :
    사실 지우지는 않고, 지우는것처럼 보이도록 값을 바꿔준다.
2. 시간복잡도 :
    O( 1 )
3. 자료구조 :
    링크드 리스트
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next=node.next.next