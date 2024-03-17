#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n ==2 :
            return 2
        a = 1
        b = 2

        for i in range(2, n):
            temp = a + b
            a = b
            b = temp

        return b