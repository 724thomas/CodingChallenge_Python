# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.next and curr.next.val == curr.next.next.val:
                last = curr.next.val
                while curr.next and curr.next.val == last:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next