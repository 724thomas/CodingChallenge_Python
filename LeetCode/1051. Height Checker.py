#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height2 = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != height2[i])