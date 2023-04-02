#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        return 1 if len([x for x in nums if x<0])%2==0 else -1