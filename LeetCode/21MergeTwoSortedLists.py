#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail=ListNode(-1)
        head=tail

        current1=list1
        current2=list2

        while current1 and current2:
            if current1.val<=current2.val:
                tail.next=current1
                current1=current1.next
            else:
                tail.next=current2
                current2=current2.next
            tail=tail.next
        tail.next = current1 if current1 else current2
        return head.next



