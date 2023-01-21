#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[0] * len(arr)
        max=-1
        for i in range(len(arr)-1,-1,-1):
            ans[i]=max
            if arr[i]>max:
                max=arr[i]
        return ans
