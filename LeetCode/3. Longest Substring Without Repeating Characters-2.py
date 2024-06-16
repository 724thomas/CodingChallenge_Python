#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)

        left = 0
        ans = 0
        for right, n in enumerate(s):
            counts[n] += 1
            while counts[n] == 2:
                counts[s[left]] -=1
                left+=1
            ans = max(ans, right-left+1)
        return ans
