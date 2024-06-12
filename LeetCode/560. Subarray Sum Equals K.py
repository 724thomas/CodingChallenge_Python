#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray = defaultdict(int)
        subarray[0] += 1
        curr = 0
        ans = 0

        for n in nums:
            curr += n
            ans += subarray[curr-k]
            subarray[curr] += 1
        return ans
