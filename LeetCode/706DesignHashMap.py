# https://leetcode.com/problems/design-hashmap/description/
'''
1. 아이디어 :
    1) 딕셔너리를 만들고, get과 remove는 try - catch로 예외 처리
2. 시간복잡도 :
    1) O(1)
3. 자료구조 :
    1) 딕셔너리
'''
class MyHashMap:

    def __init__(self):
        self.theMap = {}

    def put(self, key: int, value: int) -> None:
        self.theMap[key]=value

    def get(self, key: int) -> int:
        try:
            return self.theMap[key]
        except:
            return -1


    def remove(self, key: int) -> None:
        try:
            del self.theMap[key]
        except:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)