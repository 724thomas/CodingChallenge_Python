# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars= set()

        def check(s):
            visited = set()
            for c in s:
                if c in chars or c in visited:
                    return False
                visited.add(c)
            return True

        def backtrack(i):
            if i == len(arr):
                return len(chars)

            ans = 0
            if check(arr[i]):
                for c in arr[i]:
                    chars.add(c)
                ans = backtrack(i+1)
                for c in arr[i]:
                    chars.remove(c)

            return max(ans, backtrack(i+1))

        return backtrack(0)