# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        alist=[]
        curr=head
        while curr:
            alist.append(curr.val)
            curr=curr.next
        return alist==alist[::-1]