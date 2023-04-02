#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        count=0
        left=0
        right=k-1
        for i in range(k):
            count += nums[i]
        ans=count
        for i in range(len(nums)-k):
            count-=nums[left]
            left+=1
            right+=1
            count+=nums[right]
            ans=max(ans,count)
        return ans/k


