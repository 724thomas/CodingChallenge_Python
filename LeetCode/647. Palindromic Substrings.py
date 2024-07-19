#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        def get_pal(left, right):
            count = 0
            while left >= 0 and right<len(s) and s[left] == s[right]:
                count+=1
                left -=1
                right += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += get_pal(i,i)
            ans += get_pal(i, i+1)
        return ans