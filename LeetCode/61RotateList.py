# https://leetcode.com/problems/rotate-list/description/

'''
1. 아이디어 :
    1) 끝 노드와 첫 노드를 연결하고, k번째 노드를 찾아서 끊어준다.
2. 시간복잡도 :
    1) O(n) + O(n) = O(n)
    - 끝 노드까지의 탐색 + k번째 노드까지의 탐색
3. 자료구조 :
    1) 링크드 리스트
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr, length = head, 1
        while curr.next:
            curr=curr.next
            length+=1
        curr.next=head

        idel = length-(k%length)
        curr=head
        for i in range(idel-1):
            curr=curr.next
        head=curr.next
        curr.next=None
        return head