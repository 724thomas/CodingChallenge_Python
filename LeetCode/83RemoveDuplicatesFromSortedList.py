# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


'''
1. 아이디어 :
    1) 포인터를 두개 두고, while문을 2번 돌리면서, curr.val과 curr.next.val이 같으면 curr.next를 curr.next.next로 바꾼다.
2. 시간복잡도 :
    1) (n)
3. 자료구조 :
    1) Linked List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head

