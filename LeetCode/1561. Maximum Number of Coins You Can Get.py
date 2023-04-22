#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)[len(piles)//3:]
        return sum(piles[i] for i in range(0,len(piles),2))