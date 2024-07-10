#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles//numExchange:
            ans += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return ans
