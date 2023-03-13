#https://leetcode.com/problems/find-center-of-star-graph/description/

'''
1. 아이디어 :
    모든 edge에 공통된 숫자를 찾으면 된다.
2. 시간복잡도 :
    O(1)
3. 자료구조 :
    -
'''


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
