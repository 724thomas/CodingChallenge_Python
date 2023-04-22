#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=max2=max3=-float('inf')
        visited=set()
        for num in nums:
            if num not in visited:
                if num>max1:
                    max3=max2
                    max2=max1
                    max1=num
                elif num>max2:
                    max3=max2
                    max2=num
                elif num>max3:
                    max3=num
            visited.add(num)
            print(max1,max2,max3)
        return max(nums) if max3==-float('inf') else max3


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1=max2=max3=-float('inf')
        mlist = [-float('inf') for x in range(3)]
        for num in nums:
            if num not in mlist:
                if num>mlist[0]:
                    mlist = [num, mlist[0], mlist[1]]
                elif num>mlist[1]:
                    mlist = [mlist[0],num, mlist[1]]
                elif num>mlist[2]:
                    mlist = [mlist[0], mlist[1],num]
        return max(nums) if mlist[-1]==-float('inf') else mlist[-1]