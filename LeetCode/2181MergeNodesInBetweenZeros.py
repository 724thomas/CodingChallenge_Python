# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

'''
1. 아이디어 :
    1) 노드를 순회하면서 temp를 기록하고, 0을 만나면 배열에 저장해놓는다.
	배열에 저장된 값을 다시 원래 노드들에 저장을하고, 마지막 노드 연결을 끊는다.
2. 시간복잡도 :
	1) O(n) + O(n) = O(n)
	- 순회하며 배열에 넣기 + 배열에서 하나씩 값을 꺼내여 노드 값 재정의
3. 자료구조 :
  - 링크드리스트, 배열
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nums = []
        temp = 0
        while curr:
            if curr.val == 0 and temp!=0:
                nums.append(temp)
                temp=0
            elif curr.val !=0:
                temp+=curr.val
            curr=curr.next

        curr=head
        curr.val = nums[0]
        for i in range(1,len(nums)):
            curr=curr.next
            curr.val=nums[i]
        curr.next=None
        return head