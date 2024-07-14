#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        b = bloomDay
        if len(b) < m*k:
            return -1

        def check(day):
            ans = count = 0
            for flower in b:
                count = count + 1 if flower <= day else 0
                if count == k:
                    ans += 1
                    count = 0
            return True if ans >= m else False

        left, right = 1, max(b)

        while left<=right:
            day= (left+right) // 2
            if check(day):
                right = day-1
            else:
                left = day+ 1
        return left