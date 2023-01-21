#https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1])
        boxTypes=boxTypes[::-1]
        ans=0
        for k in boxTypes:
            while truckSize!=0 and k[0]!=0:
                ans+=k[1]
                k[0]-=1
                truckSize-=1
        return ans