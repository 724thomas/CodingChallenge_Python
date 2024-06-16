#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counter = defaultdict(int)
        c = Counter(t)
        k = len(c.keys())

        length = float('inf')
        left = right = 0
        ans = [0, 0]

        while left<len(s) or right < len(s):
            if k>0:
                if right == len(s): break
                counter[s[right]] += 1
                if counter[s[right]] == c[s[right]]:
                    k -= 1
                right += 1
            elif k == 0:
                if right-left < length:
                    length = right-left
                    ans = [left, right]
                if left == right: break
                if counter[s[left]] == c[s[left]]:
                    k += 1
                counter[s[left]] -= 1
                left+=1

        return s[ans[0]:ans[1]]
