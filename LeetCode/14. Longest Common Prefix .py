 # https://leetcode.com/problems/longest-common-prefix/description/

'''
1. 아이디어 :
    가장 짧은 strs을 기준으로,
    알파벳 하나씩 체크한다
2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    문자열
'''

 class Solution:
     def longestCommonPrefix(self, strs: List[str]) -> str:
         if len(strs)==1:
             return strs[0]

         max_length = float('inf')
         for s in strs:
             max_length = min(max_length, len(s))

         for i in range(max_length):
             base = strs[0][i]
             for w in strs:
                 if w[i]!=base:
                     return strs[0][:i]

         return strs[0][:max_length]
