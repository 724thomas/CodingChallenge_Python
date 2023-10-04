# https://leetcode.com/problems/design-linked-list/

'''
1. 아이디어 :
    링크드 리스트로 구현.
    next뿐만 아니라 prev 변수도 추가 한다.
    맨 앞에 self.left와 맨 마지막 self.right인 더미 노드를 추가해서 edge case를 없앤다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    링크드리스트
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1


    def addAtHead(self, val: int) -> None:
        cprev = self.left
        new_node = ListNode(val)
        cnext = self.left.next

        cprev.next = new_node
        new_node.next = cnext

        cnext.prev = new_node
        new_node.prev = cprev

    def addAtTail(self, val: int) -> None:
        cprev = self.right.prev
        new_node = ListNode(val)
        cnext = self.right

        cprev.next = new_node
        new_node.next = cnext

        cnext.prev = new_node
        new_node.prev = cprev


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index:
            curr = curr.next
            index -= 1
        if curr and index == 0: #Node Exist
            cprev = curr.prev
            new_node = ListNode(val)
            cnext = curr

            cprev.next = new_node
            new_node.next = cnext

            cnext.prev = new_node
            new_node.prev = cprev



    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0: #Node is before right
            cprev = curr.prev
            cnext = curr.next

            cprev.next = cnext
            cnext.prev = cprev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)