#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i, num in enumerate(arr):
            total_subarrays_containing_i = (i+1) * (n-i)
            odd_count = (total_subarrays_containing_i + 1) // 2
            ans += num * odd_count

        return ans
