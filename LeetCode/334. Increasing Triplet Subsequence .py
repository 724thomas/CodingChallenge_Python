# https://leetcode.com/problems/increasing-triplet-subsequence/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = [float('inf'), float('inf'), float('inf')]

        for n in nums:
            if n < arr[0]:
                arr[0] = n
            elif arr[0] < n < arr[1]:
                arr[1] = n
            elif arr[1] < n < arr[2]:
                arr[2] = n

        return arr[-1] != float('inf')
