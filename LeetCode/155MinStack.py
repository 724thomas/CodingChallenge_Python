#https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.alist=[]

    def push(self, val: int) -> None:
        self.alist.append(val)

    def pop(self) -> None:
        self.alist.pop()

    def top(self) -> int:
        return self.alist[-1]

    def getMin(self) -> int:
        return min(self.alist)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()