#

'''
1. 아이디어 :
    이분탐색
2. 시간복잡도 :
    O(  n log n )
3. 자료구조 :
    이분탐색
'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calc(k):
            hours = h
            for p in piles:
                hours -= ceil(p / k)
                if hours < 0:
                    return False
            return True

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if calc(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left









