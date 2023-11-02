# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

'''
1. 아이디어 :
    두 리스트의 길이가 다르면, 길이가 긴쪽의 포인터를 옮기면서 길이를 맞춰준다.
    하나씩 비교하면서 같은 노드가 나오면 리턴한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    링크들리스트
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def get_length(head):
            length = 0
            curr = head
            while curr:
                length +=1
                curr=curr.next
            return length

        length_a = get_length(headA)
        length_b = get_length(headB)
        diff = length_a - length_b
        currA = headA
        currB = headB

        if diff>0:
            for i in range(diff):
                currA = currA.next
        else:
            for i in range(-diff):
                currB = currB.next
        min_length = min(length_a, length_b)
        for i in range(min_length):
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return

