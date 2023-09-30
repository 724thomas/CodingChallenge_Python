# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

'''
1. 아이디어 :
    head 값이 5이상이면 1자리수가 늘어나기 때문에, head에 1을 추가해준다.
    그리고 head = lcurr, head.next = lnext로 잡고,
    lcurr.val = lcurr.val * 2 % 10로 계산한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    링크드리스트
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val >=5:
            head = ListNode(1,head)
            lcurr = head.next
            lnext = head.next.next
        else:
            lcurr = head
            lnext = head.next
        while lnext:
            lcurr.val = int(lcurr.val * 2 + lnext.val * 2 / 10) % 10
            lcurr = lnext
            lnext = lnext.next
        lcurr.val = lcurr.val * 2 % 10

        return head