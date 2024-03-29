# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


'''
1. 아이디어 :
    1) Constructor안에서 미리 길이를 구해놓고, getRandom()에서 랜덤으로 값을 리턴한다.
2. 시간복잡도 :
    1) Constructor: O(n), getRandom: O(1)
3. 자료구조 :
    1) Linked List

'''
import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length=0
        while head:
            self.length+=1
            head = head.next

    def getRandom(self) -> int:
        cur = self.head
        for i in range(random.randrange(0,self.length)):
            cur = cur.next
        return cur.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()