#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        queue = deque(rooms[0])

        while queue:
            room = queue.popleft()
            visited.add(room)
            keys = rooms[room]

            for k in keys:
                if k in visited:
                    continue
                queue.append(k)
        return len(visited) == len(rooms)



