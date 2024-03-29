#https://leetcode.com/problems/longest-common-subsequence/description/

'''
1. 아이디어 :
    2차 DP로 풀 수 있다.
    밑에서부터 연산하는 방식.
2. 시간복잡도 :
    O(m*n)
3. 자료구조 :
    배열
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        grid = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1,-1,-1): #text1
            for j in range(len(text2)-1,-1,-1): #text2
                if text1[i] == text2[j] :
                    grid[i][j] = 1 + grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i][j+1],grid[i+1][j])
        return grid[0][0]