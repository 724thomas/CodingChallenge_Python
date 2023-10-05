#https://leetcode.com/problems/minimum-path-sum/description/

'''
1. 아이디어 :
    dp 문제다.
    첫 row, 첫 col의 누적합을 구하고,
    [1][1] 부터 마지막까지는 왼쪽과 위 값중 작은 값을 더한다.
    grid[-1][-1]을 리턴
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col, row = len(grid[0]), len(grid)
        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]