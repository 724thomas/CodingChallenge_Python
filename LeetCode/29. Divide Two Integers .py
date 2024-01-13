# https://leetcode.com/problems/divide-two-integers/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = dividend/divisor
        if d >= 0:
            d = min(2**31-1,math.floor(d))
        else:
            d = min(2**31-1,math.ceil(d))
        return d
