#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] += 1

        for n in nums:
            total += n
            diff = total - k
            count += prefix_sums[diff]
            prefix_sums[total] +=1
        return count