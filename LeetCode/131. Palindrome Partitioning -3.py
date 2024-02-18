# https://leetcode.com/problems/palindrome-partitioning/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        memo = {}

        def is_palindrome(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            l, r = start, end
            while l < r:
                if s[l] != s[r]:
                    memo[(start, end)] = False
                    return False
                l, r = l + 1, r - 1
            memo[(start, end)] = True
            return True

        def backtrack(start, path):
            if start == len(s):
                ans.append(path.copy())
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans
