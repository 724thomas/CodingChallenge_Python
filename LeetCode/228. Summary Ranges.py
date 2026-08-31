#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []

        ans = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                end = nums[i-1]
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{end}")
                start = nums[i]

        end = nums[-1]
        if start == end:
            ans.append(str(start))
        else:
            ans.append(f"{start}->{end}")
        return ans

