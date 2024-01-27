# https://leetcode.com/problems/find-peak-element/description/

'''
1. 아이디어 :
    이분탐색으로 풀 수 있다
    왼, 중, 오를 봤을때, 왼<중 이면, 왼쪽을 버리고, 중<오 이면 오른쪽을 버린다
2. 시간복잡도 :
    O( log n )
3. 자료구조 :
    배열
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return l-1

        s = 1
        e = l-2

        while s <= e:
            mid = (s+e)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] < nums[mid]:
                s = mid + 1
            else:
                e = mid - 1
        return -1