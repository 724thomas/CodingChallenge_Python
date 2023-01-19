# https://leetcode.com/problems/search-insert-position/


'''
1. 아이디어 :
    1) 인덱스 포인터를 두고, while문을 돌리면서 인덱스 포인터를 1씩 증가 시킨다.
    2) 이분탐색으로 푼다.
2. 시간복잡도 :
    1) O(n)
    2) O(logN)
3. 자료구조 :
    1) 배열
    2) 이분탐색
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            pointer = 0
            while pointer < len(nums) and nums[pointer] < target:
                pointer += 1
            return pointer

    def searchInsert2(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return start
