#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        if n % 3 == 0:
            return 3 ** (n//3)

        if n % 3 == 1:
            return (3 ** (n//3 - 1)) * 2 * 2

        return (3 ** (n//3)) * 2