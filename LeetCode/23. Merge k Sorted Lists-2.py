#

'''
1. 아이디어 :
    LinkedList를 2개씩 Merge 합니다
    A-B, C-D, AB-CD 식으로 하게 되면 nlogk 시간이 걸립니다.
2. 시간복잡도 :
    O( nlogk )
3. 자료구조 :
    링크드 리스트
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(heada, headb):
            dummy = ListNode(-1)
            curr = dummy
            while heada and headb:
                if heada.val < headb.val:
                    curr.next = heada
                    heada = heada.next
                else:
                    curr.next = headb
                    headb = headb.next
                curr = curr.next

            if heada:
                curr.next = heada
            else:
                curr.next = headb

            return dummy.next

        if not lists:
            return None
        queue = deque(lists)
        while len(queue)>1:
            queue.append(merge(queue.popleft(), queue.popleft()))
        return queue.popleft()