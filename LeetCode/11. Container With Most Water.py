#

'''
1. 아이디어 :
    투포인터로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    상수
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0

        while l < r:
            ans = max(ans, min(height[l], height[r])*(r-l))
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return ans