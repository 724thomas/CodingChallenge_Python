#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head
        left=[]
        ans=-float("inf")
        while fast:
            left.append(slow.val)
            slow=slow.next
            fast=fast.next.next

        while left:
            ans=max(ans, slow.val+left.pop())
            slow=slow.next
        return ans
