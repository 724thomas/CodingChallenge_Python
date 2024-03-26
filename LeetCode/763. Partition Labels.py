#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i

        ans = []
        size = 0
        end = 0
        for i in range(len(s)):
            size+=1
            end = max(end, dic[s[i]])

            if i == end:
                ans.append(size)
                size = 0
        return ans


