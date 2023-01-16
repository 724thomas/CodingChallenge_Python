# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
1. 아이디어 :
    1) HashMap에 B리스트를 하나씩 넘어가면서 통째로 하나씩 넣는다.
    A리스트의 똑같은 리스트가 HashMap에 있다면, 해당 리스트를 리턴
2. 시간복잡도 :
    1) O(n) * O(n)
3. 자료구조 :
    1) 해시맵
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        numsB = set()
        while headB:
            numsB.add(headB)
            headB=headB.next

        while headA:
            if headA in numsB:
                return headA
            else:
                headA=headA.next
        return None