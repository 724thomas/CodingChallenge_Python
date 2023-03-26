#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

'''
1. 아이디어 :
    스택을 이용하여 풀 수 있다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    스택
'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        alpha=[s[0]]
        for alp in s[1:]:
            if not alpha or alpha[-1]!=alp:
                alpha.append(alp)
            elif alpha[-1]==alp:
                alpha.pop()

        return "".join(alpha)
