#https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/submissions/

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3!=0:
            return False
        avg=int(sum(arr)/3)
        part, cnt = 0,0
        for num in arr:
            part+=num
            if part==avg:
                part=0
                cnt+=1
        return cnt>=3
        