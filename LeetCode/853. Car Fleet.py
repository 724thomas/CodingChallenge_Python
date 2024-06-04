#

'''
1. 아이디어 :
    easy
2. 시간복잡도 :
    O( n log n )
3. 자료구조 :
    해시셋
'''


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = set()
        cars = sorted(list(zip(position, speed)),reverse=True)

        front = 0
        for p, s in cars:
            front = max(front, (target-p)/s)
            fleets.add(front)
        return len(fleets)