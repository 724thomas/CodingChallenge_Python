# https://leetcode.com/problems/sum-of-square-numbers/description/

'''
1. 아이디어 :
    투 포인터 사용
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    -
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)
        while left <= right:
            total = left * left + right * right
            if total < c:
                left += 1
            elif total > c:
                right -= 1
            else:
                return True
        return False
