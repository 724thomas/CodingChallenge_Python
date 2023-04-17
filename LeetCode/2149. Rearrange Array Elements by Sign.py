#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)

        for i in range(len(pos)):
            ans.append(neg.pop())
            ans.append(pos.pop())
        return ans[::-1]