#https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cprev=None
        curr=head

        while curr:
            cnext=curr.next
            curr.next=cprev
            cprev=curr
            curr=cnext

        return cprev
