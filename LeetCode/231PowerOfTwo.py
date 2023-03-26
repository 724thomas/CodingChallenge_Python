#https://leetcode.com/problems/power-of-two/

'''
1. 아이디어 :
    2의 제곱수는 2진수로 표현했을 때 1이 한번만 나타난다.
2. 시간복잡도 :
    O(logn)
3. 자료구조 :
    문자열
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        start=1
        while start<n:
            start*=2
            if start==n:
                return True
        return False