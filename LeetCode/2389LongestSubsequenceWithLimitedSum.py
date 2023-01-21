#https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for i in queries:
            index=0
            count=0
            while index<len(nums):
                count+=nums[index]
                index+=1
                if count>i:
                    index-=1
                    break
                elif count==i:
                    break
            ans.append(index)
        return ans