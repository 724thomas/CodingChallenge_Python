#

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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lDummy=ListNode(-1)
        hDummy=ListNode(-1)
        lcur=lDummy
        hcur=hDummy

        curr=head
        while curr:
            if curr.val>=x:
                hcur.next=curr
                hcur=hcur.next
            else:
                lcur.next=curr
                lcur=lcur.next
            curr=curr.next
        hcur.next=None
        lcur.next=hDummy.next
        return lDummy.next