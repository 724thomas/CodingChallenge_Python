#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def ArrayToLinkedList(head):
    if not head:
        return None
    node = ListNode(head[0])
    node.next = createLinkedList(head[1:])
    return node


change_this = ArrayToLinkedList(change_this)




head = [1,2,3,3,4,5]
answer = [1,2,3]

