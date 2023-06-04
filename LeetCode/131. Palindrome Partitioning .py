# https://leetcode.com/problems/palindrome-partitioning/description/

'''
1. 아이디어 :
    백트래킹을 사용하여 s[k:i+1]이 팰린드롬이면, cList에 추가하고, i+1부터 재귀호출을 한다.
2. 시간복잡도 :
    O(N!)
3. 자료구조 :
    리스트
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(cList=[], k=0):
            if k == len(s):
                ans.append(cList)
                return

            for i in range(k, len(s)):
                temp = s[k:i +1]
                if temp == temp[::-1]:
                    backtrack(cList + [temp], i+1)


        backtrack()
        return ans

