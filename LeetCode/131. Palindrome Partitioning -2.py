# https://leetcode.com/problems/palindrome-partitioning/description/

'''
1. 아이디어 :
    memoization을 통해 palindrome 여부를 저장할수도 있다.
    백트래킹 사용
2. 시간복잡도 :
    O(n * n^2)
3. 자료구조 :
    배열
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(idx, arr):
            if idx==len(s):
                ans.append(arr)
                return

            for i in range(idx, len(s)):
                string = s[idx:i+1]
                if string == string[::-1]:
                    backtrack(i+1, arr+[string])

        backtrack(0, [])
        return ans