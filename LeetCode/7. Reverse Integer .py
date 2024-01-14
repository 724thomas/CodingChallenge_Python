# https://leetcode.com/problems/reverse-integer/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O( 1 )
3. 자료구조 :

'''

class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x = int(str(x)[::-1])
            return 0 if x <= -2**31 or x>= 2**31-1 else x
        else:
            x = int(str(-x)[::-1])
            return 0 if -x <= -2**31 or -x>= 2**31-1 else -x