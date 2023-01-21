# https://leetcode.com/problems/island-perimeter/description/

'''
1. 아이디어 :
    2중 for문으로, 해당 좌표가 1일경우, 4방향을 확인해서 닿는 땅이 몇개인지 계산하여, (4방향-땅 개수)를 모두 합한다
2. 시간복잡도 :
    1) O(n^2)
    - 2중 포문
3. 자료구조 :
    1) 2차원 배열
'''


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def CountSurround(x, y, grid) -> int:
            xmax = len(grid) - 1
            ymax = len(grid[0]) - 1
            count = 0
            if 0 <= x - 1 <= xmax and grid[x - 1][y] == 1:
                count += 1
            if 0 <= x + 1 <= xmax and grid[x + 1][y] == 1:
                count += 1
            if 0 <= y - 1 <= ymax and grid[x][y - 1] == 1:
                count += 1
            if 0 <= y + 1 <= ymax and grid[x][y + 1] == 1:
                count += 1
            return count

        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    print(x, y, CountSurround(x, y, grid))
                    ans += 4 - CountSurround(x, y, grid)
        return ans
