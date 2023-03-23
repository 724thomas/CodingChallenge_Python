#https://leetcode.com/problems/degree-of-an-array/

'''
1. 아이디어 :
    Counter를 이용해서 각 숫자의 빈도수를 구하고 가장 높은 빈도수를 가진 숫자들을 구한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    리스트, 해시맵
'''


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a=Counter(nums)
        print(a)
        cmax=0
        candid=[]
        for key,val in a.items():
            cmax=max(cmax,val)
        for key,val in a.items():
            if val==cmax:
                candid.append(key)

        cmin=float('inf')
        l=0
        r=0
        for j in candid:
            for i in range(len(nums)-1):
                if nums[i]==j:
                    l=i
                    break
            for i in range(len(nums)-1,-1,-1):
                if nums[i]==j:
                    r=i
                    break
            cmin=min(cmin,r-l+1)
        return cmin
