# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        characters = {"2":"abc",
                      "3":"def",
                      "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz"
                      }

        ans = []
        temp = []

        def backtrack(i):
            if i==len(digits):
                ans.append("".join(temp))
                return

            for c in characters[digits[i]]:
                temp.append(c)
                backtrack(i+1)
                temp.pop()

        backtrack(0)
        return ans
