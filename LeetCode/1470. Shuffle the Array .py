# https://leetcode.com/problems/shuffle-the-array/description/

'''
1. 아이디어 :
    투포인터로 x1과 y1을 len(nums)//2 만큼 반복하면서 ans에 append 한다
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x1, y1 = 0, len(nums)//2
        ans = []
        for i in range(len(nums)//2):
            ans.append(nums[x1])
            ans.append(nums[y1])
            x1+=1
            y1+=1
        return ans