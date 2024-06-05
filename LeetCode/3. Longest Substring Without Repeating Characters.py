#

'''
1. 아이디어 :
ㅤㅤ슬라이딩 윈도우를 사용한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
ㅤㅤ해시셋
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        visited = set()
        l = 0
        r = 0

        while r<len(s):
            if s[r] not in visited:
                visited.add(s[r])
                r+=1
            else:
                visited.remove(s[l])
                l+=1
            ans = max(ans, r-l)
        return ans