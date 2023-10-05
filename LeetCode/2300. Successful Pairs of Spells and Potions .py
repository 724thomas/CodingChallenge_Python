# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

'''
1. 아이디어 :
    이분탐색으로 각 spell이 success되는 최소값을 찾는다.
2. 시간복잡도 :
    nlogm + mlogm
    spells * 이분탐색 + 정렬
3. 자료구조 :
    배열
'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def binary_search(min_num, potions):
            left = 0
            right = len(potions)-1

            while left <= right:
                mid = (left+right)//2
                if potions[mid] >= min_num:
                    right = mid - 1
                else:
                    left = mid + 1
            return len(potions)-right-1

        potions.sort()
        ans = []
        for n in spells:
            ans.append(binary_search(math.ceil(success/n),potions))
        return ans