#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        candid=set()
        counts={}
        for n in nums:
            if n not in counts:
                counts[n]=1
                candid.add(n)
            else:
                counts[n]+=1
            if counts[n]==3:
                candid.remove(n)
        return list(candid)[0]