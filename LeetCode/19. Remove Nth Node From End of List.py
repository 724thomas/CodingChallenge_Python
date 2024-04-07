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
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next

        if n==len(nodes):
            return head.next
        if -n+1<0:
            nodes[-n-1].next=nodes[-n+1]
        else:
            nodes[-n-1].next=None

        return head