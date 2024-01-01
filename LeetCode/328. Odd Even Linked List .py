# https://leetcode.com/problems/odd-even-linked-list/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)
        odd = dummy_odd
        even = dummy_even

        is_odd = True
        while curr:
            if is_odd:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            is_odd = not is_odd
            curr=curr.next

        even.next = None
        odd.next = dummy_even.next
        return dummy_odd.next



