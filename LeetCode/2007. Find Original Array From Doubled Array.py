#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        c = Counter(changed)
        ans = []

        for n in changed:
            if c[n] == 0:
                continue
            if c[n*2] == 0:
                return []
            ans.append(n)
            if n == 0 and c[n] <= 1:
                return []
            c[n] -= 1
            c[n*2] -= 1
        return ans