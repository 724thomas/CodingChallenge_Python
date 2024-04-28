#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class MinStack:

    def __init__(self):
        self.base_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.base_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.base_stack.pop()
        if self.min_stack[-1] == popped:
            self.min_stack.pop()

    def top(self) -> int:
        return self.base_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()