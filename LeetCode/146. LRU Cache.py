#

'''
1. 아이디어 :

2. 시간복잡도 :
    O( 1 )
3. 자료구조 :

'''


class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = LinkedListNode(-1, -1)
        self.tail = LinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete_first(self):
        if self.head.next == self.tail:
            return #비어있음

        first_node = self.head.next
        self._delete_node(first_node)
        del self.map[first_node.key]

    def _update(self, node):
        self._delete_node(node)
        self._append_last(node)

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append_last(self, node):
        right = self.tail
        left = self.tail.prev
        left.next = node
        node.next = right
        right.prev = node
        node.prev = left

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._update(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            existing_node = self.map[key]
            existing_node.val = value
            self._update(existing_node)
        else:
            if len(self.map) >= self.capacity:
                self._delete_first()
            new_node = LinkedListNode(key, value)
            self.map[key] = new_node
            self._append_last(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)