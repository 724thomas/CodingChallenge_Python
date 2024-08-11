#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = defaultdict(int)
        total = 0
        for i, n in enumerate(nums):
            total = (total + n) % k
            if total == 0 and i >= 1:
                return True
            if total not in remainders:
                remainders[total] = i
            elif i - remainders[total] >= 2:
                return True
        return False

