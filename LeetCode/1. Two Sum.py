#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = i
        for i, n in enumerate(nums):
            if target-n in dic and i!=dic[target-n]:
                return [i, dic[target-n]]
