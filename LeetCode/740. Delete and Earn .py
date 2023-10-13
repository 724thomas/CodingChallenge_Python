# https://leetcode.com/problems/delete-and-earn/description/

'''
1. 아이디어 :
    DP문제
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0

        for i in range(len(nums)):
            curEarn = nums[i] * c[nums[i]]

            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2
