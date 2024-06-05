#

'''
1. 아이디어 :
    two pointer를 이용하여 풀이
2. 시간복잡도 :
    O( n^2 )
3. 자료구조 :
    배열
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            l = i+1
            r = len(nums)-1

            while l<r:
                total = nums[l] + nums[r]
                if total == target:
                    ans.append([nums[i],nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < target:
                    l += 1
                elif total > target:
                    r -= 1
        return ans