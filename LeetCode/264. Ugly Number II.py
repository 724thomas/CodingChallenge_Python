#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0

        for i in range(n):
            min_val = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(min_val)

            if min_val == nums[i2] * 2:
                i2 += 1
            if min_val == nums[i3] * 3:
                i3 += 1
            if min_val == nums[i5] * 5:
                i5 += 1

        return nums[n-1]