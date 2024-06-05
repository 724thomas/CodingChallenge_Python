#

'''
1. 아이디어 :
ㅤㅤ투 포인터로 둔다.
    왼쪽 최대값, 오른쪽 최대값을 통해, 해당 인덱스(1칸)에 물이 찰 수 있는 양을 계산한다.
    더 작은 쪽을 이동시켜가며 계산한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
ㅤㅤ상수
'''


from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                l+=1
                lmax = max(lmax, height[l])
                ans += lmax - height[l]
            else:
                r-=1
                rmax = max(rmax, height[r])
                ans += rmax - height[r]

        return ans


