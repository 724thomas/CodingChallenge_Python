#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

'''
1. 아이디어 :
    힙 사용
2. 시간복잡도 :
    NlogN
3. 자료구조 :
    힙
'''



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        return (heapq.heappop(nums) + 1) * (heapq.heappop(nums) + 1)