#https://leetcode.com/problems/jump-game-ii/

'''
1. 아이디어 :
    최대로 갈 수 있는 범위를 구하고, 그 범위만큼 다음 범위를 구한다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    -
'''

res = 0
l = r = 0

class Solution:
    def jump(self, nums: List[int]) -> int:

        ans = 0
        l = r = 0

        while r<len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+ nums[i])
            l = r+1
            r = farthest
            ans+=1

        return ans