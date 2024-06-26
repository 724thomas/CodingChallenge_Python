#

'''
1. 아이디어 :

2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()

        left = 0
        right = len(nums)-1


        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
