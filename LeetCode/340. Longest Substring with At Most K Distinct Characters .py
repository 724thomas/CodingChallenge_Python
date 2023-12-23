# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

'''
1. 아이디어 :
    투포인터와 해시맵을 사용한다.
    distinct보다 작거나 같으면 right 포인터를, 아니면 left 포인터를 이동시킨다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열, 해시맵
'''

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0

        distinct = left = right = ans = 0
        hmap = defaultdict(int)

        while right<len(s):
            if distinct<=k:
                ans = max(ans, right-left)
            if distinct <= k:
                hmap[s[right]]+=1
                if hmap[s[right]] == 1:
                    distinct+=1
                right+=1
            else:
                hmap[s[left]]-=1
                if hmap[s[left]] == 0:
                    distinct-=1
                left+=1

        if distinct<=k:
            ans = max(ans, right-left)


        return ans