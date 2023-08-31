#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es=sum(nums)
        ds= sum([int(x) for x in ("".join(list(map(str,nums))))])
        return abs(es-ds)