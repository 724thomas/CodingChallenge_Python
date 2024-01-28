# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

'''
1. 아이디어 :
    이분탐색을 두번한다
2. 시간복잡도 :
    O( log n )
3. 자료구조 :
    배열
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        s = 0
        e = len(nums)-1

        while s<=e:
            mid = (s+e)//2
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1

        ans = [s]
        target += 1
        s = 0
        e = len(nums)-1
        while s<=e:
            mid = (s+e)//2
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1

        ans.append(e)
        return [-1,-1] if ans[0] > ans[1] else ans
