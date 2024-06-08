#

'''
1. 아이디어 :
    이분탐색을 한다.
    nums[left] < nums[right]부분이 중요한데, 이는 left가 최소값이라는 것을 의미한다.
2. 시간복잡도 :
    O(  log n )
3. 자료구조 :
    이분탐색
'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                ans = min(ans, nums[left])
                break

            mid = (left+right)//2
            ans = min(ans, nums[mid])

            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid

        return ans


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]