# https://leetcode.com/problems/reverse-linked-list/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cpre = None
        curr = head

        while curr:
            cnex = curr.next
            curr.next = cpre
            cpre = curr
            curr = cnex
        return cpre

