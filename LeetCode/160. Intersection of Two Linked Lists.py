#

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()

        while headA:
            node_set.add(headA)
            headA = headA.next

        while headB:
            if headB in node_set:
                return headB
            else:
                headB = headB.next