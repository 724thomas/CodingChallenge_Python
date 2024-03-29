#https://leetcode.com/problems/keys-and-rooms/

'''
1. 아이디어 :
    BFS로 풀 수 있다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시셋, 큐
'''


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        open = set()
        open.add(0)
        keylist = deque()
        keylist.append(rooms[0])

        while keylist:
            keys = keylist.popleft()
            for key in keys:
                if key not in open:
                    open.add(key)
                    keylist.append(rooms[key])
        return len(rooms) == len(open)