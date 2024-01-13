# https://leetcode.com/problems/unique-paths-ii/description/

'''
1. 아이디어 :
    dp 사용
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :

'''

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            if grid[i][0] != 1:
                dp[i][0] = 1
            else:
                break
        for i in range(len(grid[0])):
            if grid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                if grid[row][col] != 1:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]