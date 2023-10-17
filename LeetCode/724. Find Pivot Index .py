# https://leetcode.com/problems/find-pivot-index/description/

'''
1. 아이디어 :
    left, right의 합을 트래킹하고 idx를 하나씩 옮기면서 확인
    # 이분탐색은 음수가 있어서 안된다.
2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        idx = 0
        if left == right:
            return 0

        while idx < len(nums) - 1:
            left += nums[idx]
            idx += 1
            right -= nums[idx]
            if left == right:
                return idx
        return -1
