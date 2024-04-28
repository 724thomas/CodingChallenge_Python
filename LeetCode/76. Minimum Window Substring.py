# https://leetcode.com/problems/minimum-window-substring/description/

'''
1. 아이디어 :
    t_map에 Counter(t)로 t의 각 문자의 개수를 저장한다.
    투포인터를 사용해서 s_map에 s의 각 문자를 저장한다
    s_map과 t_map을 비교하는데, 각 원소들을 다 확인하면 시간복잡도가 n이므로, needed 변수를 통해 확인한다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    해시맵
'''

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for c in t:
            t_map[c]+=1

        needed = len(t_map.keys())
        left = right = 0
        ans = [float('inf'), s[left:right]]

        while right<len(s) or left<len(s):
            if needed:
                if right == len(s):
                    break
                if s[right] in t_map:
                    s_map[s[right]] += 1
                    if s_map[s[right]] == t_map[s[right]]:
                        needed -= 1
                right+=1

            else:
                if right-left < ans[0]:
                    ans = [right-left, s[left:right]]
                if s[left] in t_map:
                    if s_map[s[left]] == t_map[s[left]]:
                        needed += 1
                    s_map[s[left]] -= 1
                left+=1

        return ans[1]
