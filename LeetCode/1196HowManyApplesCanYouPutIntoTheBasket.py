#https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        b=5000
        weight=sorted(weight)
        cnt=0
        for apple in weight:
            if b>=apple:
                b-=apple
                cnt+=1
        return cnt