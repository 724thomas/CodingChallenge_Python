#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''
1. 아이디어 :
    1) 총 노드의 길이를 구하고, 앞에서 몇번째 인덱스인지 구한 후,
    탐색하며 직전 인덱스의 노드를 다음.다음 노드와 연결.
2. 시간복잡도 :
    1) O(n) + O(n) = O(n)
    - 길이 탐색 + 해당 노드 탐색
3. 자료구조 :
    1) 링크드 리스트
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1
        idel = count-n

        if idel==0:
            return head.next if head.next else None

        curr=head
        for i in range(idel-1):
            curr=curr.next
        curr.next=curr.next.next if curr.next.next else None

        return head