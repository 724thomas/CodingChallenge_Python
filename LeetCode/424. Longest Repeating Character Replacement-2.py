#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = right = 0
        ans = 0
        while right < len(s):
            counts[s[right]] += 1
            right+=1

            while right - left - max(counts.values()) > k:
                counts[s[left]] -= 1
                left+=1
            ans = max(ans, right-left)
        return ans