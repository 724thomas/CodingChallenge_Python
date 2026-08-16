#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)

        curr = head
        while curr:
            freq[curr.val] += 1
            curr = curr.next

        dummy = ListNode()
        tail = dummy

        for count in freq.values():
            tail.next = ListNode(count)
            tail = tail.next

        return dummy.next