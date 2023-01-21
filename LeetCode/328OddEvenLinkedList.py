#https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        odd=head
        even=odd.next
        evenh=even

        while odd.next and even.next:
            odd.next=even.next
            odd=even.next
            even.next=odd.next
            even=odd.next
        odd.next=evenh
        return head