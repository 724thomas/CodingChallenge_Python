#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp=0
        rp=len(height)-1
        max=0
        while lp<rp:
            temp=area(height[lp],height[rp],rp-lp)
            if temp>max:
                max=temp
            if height[lp]>height[rp]:
                rp-=1
            else:
                lp+=1
        return max

def area(left, right, length):
    return min(left,right)*length