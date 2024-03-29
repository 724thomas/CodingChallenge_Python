#https://leetcode.com/problems/design-hashmap/description/

'''
1. 아이디어 :
    배열로 만든다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class MyHashMap:

    def __init__(self):
        self.nums = [-1] * (10**6+1)

    def put(self, key: int, value: int) -> None:
        self.nums[key] = value

    def get(self, key: int) -> int:
        return self.nums[key] if self.nums[key]!=-1 else -1

    def remove(self, key: int) -> None:
        self.nums[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)