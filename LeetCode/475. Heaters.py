#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        heaters=[float('-inf')]+heaters+[float('inf')]
        ans = i = 0

        for house in houses:
            while house > heaters[i+1]:
                i += 1
            dis = min(house - heaters[i], heaters[i+1] - house)
            ans = max(ans, dis)
        return ans