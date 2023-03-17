# https://leetcode.com/problems/middle-of-the-linked-list/description/

'''
1. 아이디어 :
    1) 리스트를 순회하면서 리스트의 길이를 구하고, 리스트의 길이를 2로 나눈 인덱스의 원소를 리턴
    2) 두개의 포인터를 사용하여, slow, fast를 두고, fast가 끝에 도달하면 slow를 리턴.
2. 시간복잡도 :
    1) O(N)
    2) O(N)
3. 자료구조 :
    1) 배열
    2) 링크드리스트
'''


# 1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        alist = []
        while curr:
            alist.append(curr)
            count += 1
            curr = curr.next
        mid = count // 2
        return alist[mid]


# 2)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast.next else slow
