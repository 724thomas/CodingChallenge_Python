# https://leetcode.com/problems/implement-stack-using-queues/description/

'''
1. 아이디어 :
    Deque를 활용했다.
2. 시간복잡도 :
    1. push : O(1)
    2. pop : O(1)
    3. top : O(1)
    4. empty : O(1)
3. 자료구조 :
    1. Deque
'''


class MyStack:

    def __init__(self):
        self.queue1 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return False if self.queue1 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()