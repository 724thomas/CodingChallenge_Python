#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        base = Counter(p)

        dic = defaultdict(int)
        for i in range(len(p)):
            dic[s[i]] += 1
        if dic == base:
            ans.append(0)

        left = 0
        right = len(p)
        while right < len(s):
            dic[s[left]] -=1
            if dic[s[left]] == 0:
                del dic[s[left]]
            dic[s[right]] += 1
            left+=1
            right+=1
            if dic == base:
                ans.append(left)

        return ans

