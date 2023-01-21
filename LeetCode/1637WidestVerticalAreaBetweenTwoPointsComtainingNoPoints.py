# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        alist=sorted([x[0] for x in points])
        cmax=0
        for i in range(len(alist)-1):
            cmax = max(cmax,alist[i+1]-alist[i])
        return cmax