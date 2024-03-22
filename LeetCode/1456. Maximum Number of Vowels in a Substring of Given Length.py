#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        vowels = set(['a','e','i','o','u'])
        cmax = 0
        for i in range(k):
            if s[i] in vowels:
                cmax+=1
        curr = cmax
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr+=1
            if s[i-k] in vowels:
                curr-=1
            cmax = max(cmax, curr)
        return cmax