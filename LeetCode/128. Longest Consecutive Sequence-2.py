#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        cmax = 0
        visited = set()

        for n in nset:
            if n not in visited:
                visited.add(n)
                i = 0
                while n+i in nset:
                    visited.add(n+i)
                    i+=1
                cmax = max(cmax, i)
        return cmax