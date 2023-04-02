#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l=[0]
        r=[0]
        for i in range(1,len(nums)):
            l.append(nums[i-1]+l[-1])
            r.append(nums[-i]+r[-1])
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(l[i]-r[-i-1]))
        return ans
