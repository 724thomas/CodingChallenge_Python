# https://leetcode.com/problems/linked-list-cycle/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(-1)
        dummy.next=head
        slow=dummy
        fast=dummy

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True

        return False
