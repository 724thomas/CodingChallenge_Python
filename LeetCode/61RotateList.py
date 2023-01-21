# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr=head
        length=1
        while curr.next:
            curr=curr.next
            length+=1
        curr.next=head
        idel = length-(k%length)
        curr=head
        for i in range(idel-1):
            curr=curr.next
        head=curr.next
        curr.next=None
        return head