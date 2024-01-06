# https://leetcode.com/problems/merge-k-sorted-lists/description/

'''
1. 아이디어 :
    링크드 리스트를 합치는 메서드.
    [a,b,c,d]가 있을때, ((a+b)+c)+d가 아닌, (a+b) + (c+d) 방식으로 했다
2. 시간복잡도 :
    O(n*m)
3. 자료구조 :
    큐
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

        lists = deque(lists)

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


        while len(lists) >= 2:
            listA = lists.popleft()
            listB = lists.popleft()
            lists.append(merge(listA, listB))
        return lists.popleft()