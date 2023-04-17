#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def partitionString(self, s: str) -> int:
        ans=0
        exist=""
        for i in range(len(s)):
            if s[i] not in exist:
                exist+=s[i]
            else:
                ans+=1
                exist=s[i]
        return ans +1 if exist else ans
