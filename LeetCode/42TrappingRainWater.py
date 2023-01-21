class Solution:

    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        clmax = 0
        crmax=0
        for i in range(len(height)-1):
            lmax[i+1] = clmax = max(clmax,height[i])
            rmax[i+1] = crmax = max(crmax,height[-1-i])
        rmax = rmax[::-1]
        for i in range(len(height)):
            height[i] = max(min(lmax[i],rmax[i])-height[i], 0 )
        return sum(height)