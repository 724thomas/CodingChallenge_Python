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
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def get_mid_node(head):
            dummy = ListNode(-1)
            dummy.next = head
            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return mid

        def reverse_linked_list(head):
            prev = None
            curr = head

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev


        def combine_linked_list(list1, list2):
            while list2:
                next1 = list1.next
                next2 = list2.next

                list1.next = list2
                list2.next = next1

                list1 = next1
                list2 = next2


        mid = get_mid_node(head)
        mid = reverse_linked_list(mid)
        return combine_linked_list(head, mid)