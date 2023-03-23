# https://leetcode.com/problems/word-pattern/

'''
1. 아이디어 :
    해시맵을 두개 만들어서 각각의 문자열과 패턴을 매핑한다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        hm1={}
        hm2={}
        s=s.split(" ")
        if len(p)!=len(s):
            return False
        for i in range(len(p)):
            if p[i] not in hm1:
                hm1[p[i]]=s[i]
            elif p[i] in hm1:
                if hm1[p[i]]!=s[i]:
                    return False

            if s[i] not in hm2:
                hm2[s[i]]=p[i]
            elif s[i] in hm2:
                if hm2[s[i]]!=p[i]:
                    return False
            print(hm1)
            print(hm2)
        return True