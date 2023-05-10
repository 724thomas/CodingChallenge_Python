# https://leetcode.com/problems/merge-in-between-linked-lists/description/

'''
1. 아이디어 :
    1) b까지 돌면서 a-1 인덱스가 나오면 start로 저장해놓는다.
       b인덱스까지 가게되면 그 다음 원소를 end로 저장해놓는다.
       start 뒤에 list2를 이어붙이고, list2의 마지막원소까지 탐색한 후, 그 뒤에 end를 붙인다.
2. 시간복잡도 :
    1) O(N)
3. 자료구조 :
    1) 링크드리스트
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        for i in range(b):
            if i == a - 1:
                start = curr
            curr = curr.next
        end = curr.next

        start.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = end

        return list1
