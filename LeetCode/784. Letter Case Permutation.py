# https://leetcode.com/problems/letter-case-permutation/description/

'''
1. 아이디어 :
    백트래킹을 사용하여, s[i]가 알파벳이면, 대문자와 소문자를 각각 추가하여 재귀호출을 한다.
2. 시간복잡도 :
    O(N!)
3. 자료구조 :
    리스트
'''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        l = len(s)

        def backtrack(p = "", idx= 0, length = 0):
            if length==l:
                ans.append(p)
                return

            if s[idx].isalpha() and ord(s[idx])<96:
                backtrack(p+s[idx].lower(), idx+1, length+1)
            elif s[idx].isalpha() and ord(s[idx])>=96:
                backtrack(p+s[idx].upper(), idx+1, length+1)

            backtrack(p+s[idx], idx+1, length+1)


        backtrack("",0, 0)
        return ans
