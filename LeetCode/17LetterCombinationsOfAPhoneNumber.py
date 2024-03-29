#https://leetcode.com/problems/letter-combinations-of-a-phone-number/

'''
1. 아이디어 :
    브루트포스로는 시간 초과가 나기때문에 백트래킹을 사용한다.
2. 시간복잡도 :
    O(4^4)
    digit은 최대 4 Character가 있고, 각 character는 최대 4개의 alphabet이 있다.
3. 자료구조 :
    배열, 해시맵
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        characters = {"2":"abc",
                      "3":"def",
                      "4":"ghi",
                      "5":"jkl",
                      "6":"mno",
                      "7":"pqrs",
                      "8":"tuv",
                      "9":"wxyz"
                      }
        temp = []
        def backtracking(i):
            if len(temp)==len(digits):
                ans.append(temp.copy())
                return

            for c in characters[digits[i]]:
                temp.append(c)
                backtracking(i+1)
                temp.pop()

        backtracking(0)
        for i in range(len(ans)):
            ans[i] = "".join(ans[i])
        return ans

