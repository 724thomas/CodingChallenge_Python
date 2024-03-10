#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1]*n

        for row in range(m-1):
            for col in range(1, n):
                grid[col] += grid[col-1]

        return grid[-1]