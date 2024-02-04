# https://leetcode.com/problems/merge-two-sorted-lists/description/

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        p3 = dummy = ListNode(-1)
        while p1 and p2:
            if p1.val < p2.val:
                p3.next = p1
                p1=p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next

        if p1:
            p3.next = p1
        elif p2:
            p3.next = p2

        return dummy.next