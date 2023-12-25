# https://leetcode.com/problems/single-number/description/

'''
1. 아이디어 :
    ^ 연산 이해가 안됨...
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    O(n)
'''

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for key, val in c = Counter(nums).items():
            if val==1:
                return key

        '''
        xor = 0
        for n in nums:
            xor = n ^ xor
        return xor
        '''

