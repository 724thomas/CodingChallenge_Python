#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        c = defaultdict(int)
        included = set(arr2)
        rest = []
        for n in arr1:
            if n not in included:
                rest.append(n)
            c[n] += 1

        for n in arr2:
            while c[n] != 0:
                ans.append(n)
                c[n] -= 1
        rest.sort()
        ans += rest
        return ans
