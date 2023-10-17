# https://leetcode.com/problems/design-hashset/description/

'''
1. 아이디어 :
    limit까지 배열을 -1로 초기화 한다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class MyHashSet:

    def __init__(self):
        self.nums = [-1] * (10**6+1)

    def add(self, key: int) -> None:
        self.nums[key] = 1

    def remove(self, key: int) -> None:
        self.nums[key] = -1

    def contains(self, key: int) -> bool:
        return True if self.nums[key] == 1 else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)