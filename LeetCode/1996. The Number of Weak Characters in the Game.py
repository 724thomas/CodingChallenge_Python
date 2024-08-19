#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import Counter
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x : (x[0], -x[1]))
        ans = 0
        stack = []
        for p in properties:
            while stack and stack[-1][0] < p[0] and stack[-1][1] < p[1]:
                stack.pop()
                ans += 1
            stack.append(p)
        return ans