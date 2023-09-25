# https://leetcode.com/problems/car-fleet/description/

'''
1. 아이디어 :
    도착하는데에 얼마나 걸릴지 앞에서부터 계산하고,
    뒤 차가 앞 자보다 빠르면 앞 차가 뒤 차를 따라잡을 수 없으므로 fleets 스택에 추가하고,
    그게 아니면 추가하지 않는다.
2. 시간복잡도 :
    O(NlogN)
3. 자료구조 :
    스택
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets=[]

        cars = sorted([[position[i],speed[i]] for i in range(len(position))], reverse=True)

        for p,s in cars:
            fleets.append((target-p)/s)
            if len(fleets)>=2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)


