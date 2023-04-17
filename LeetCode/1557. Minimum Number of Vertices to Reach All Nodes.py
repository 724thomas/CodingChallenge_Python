#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nums={x for x in range(n)}
        for e in edges:
            if e[1] in nums:
                nums.remove(e[1])
        return list(nums)