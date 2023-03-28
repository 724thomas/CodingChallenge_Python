#https://leetcode.com/problems/ransom-note/description/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        rc=Counter(r)
        mc=Counter(m)

        for k, v in rc.items():
            if mc[k]<v:
                return False
        return True