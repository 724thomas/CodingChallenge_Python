# https://leetcode.com/problems/sort-list/description/

'''
1. 아이디어 :
    list를 합치는것, list의 중간을 가져오는 메서드를 만든다.
    sort_list를 recursive를 통해, 정렬한다
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    링크드리스트
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_mid_list(list1):
            slow, fast = list1, list1.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge_list(list1, list2):
            dummy = curr = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            curr.next = list1 or list2
            return dummy.next

        def sort_list(list1):
            if not list1 or not list1.next:
                return list1

            left = list1
            right = get_mid_list(list1)
            temp = right.next
            right.next = None
            right = temp

            left = sort_list(left)
            right = sort_list(right)
            return merge_list(left, right)

        return sort_list(head)






