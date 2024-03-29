# https://leetcode.com/problems/di-string-match/description/

'''
1. 아이디어 :
    최대값을 길이만큼, 최소값을 0부터 시작해서, D가 나오면 최대값을 넣은 후 1 감소시키고, I가 나오면 반대로.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        cmax = len(s)
        cmin = 0
        ans = []

        for letter in s:
            if letter == "D":
                ans.append(cmax)
                cmax-=1
            else:
                ans.append(cmin)
                cmin+=1
        ans.append(cmax)
        return ans