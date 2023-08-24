#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[int(n) for n in nums]
        nums.sort(reverse=True)
        return str(nums[k-1])