#

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
from collections import deque
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        def merge(lista, listb):
            dummy = curr = ListNode(0)

            while lista and listb:
                if lista.val < listb.val:
                    curr.next = lista
                    lista = lista.next
                else:
                    curr.next = listb
                    listb = listb.next
                curr = curr.next
            curr.next = lista or listb

            return dummy.next


        lists = deque(lists)

        while len(lists) >= 2:
            listA = lists.popleft()
            listB = lists.popleft()
            lists.append(merge(listA, listB))
        return lists.popleft()