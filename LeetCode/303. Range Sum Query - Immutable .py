# https://leetcode.com/problems/range-sum-query-immutable/description/

'''
1. 아이디어 :
    누적합을 사용
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cum = [0]
        for i in range(len(nums)):
            self.cum.append(self.cum[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.cum[right+1]-self.cum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)