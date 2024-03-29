#https://leetcode.com/problems/valid-parentheses/description/

'''
1. 아이디어 :
    - 스택을 사용하여 풀이.
2. 시간복잡도 :
    - O(n) : n은 s의 길이
3. 자료구조 :
    - 스택
'''


class Solution:
    def isValid(self, s: str) -> bool:
        chars = [s[0]]
        for i in range(1,len(s)):
            if len(chars)==0:
                chars.append(s[i])
            else:
                if s[i] == "]" and chars[-1] == "[":
                    chars.pop()
                elif s[i] == "}" and chars[-1] == "{":
                    chars.pop()
                elif s[i] == ")" and chars[-1] == "(":
                    chars.pop()
                else:
                    chars.append(s[i])

        return True if len(chars)==0 else False