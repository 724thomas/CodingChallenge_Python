#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        print(*grid, sep='\n')
        if n<3 or m<3:
            return 0

        def check(row, col):
            visited = set(range(1, 10))
            pos = neg = 0
            rows = [0,0,0]
            cols = [0,0,0]
            for x in range(3):
                for y in range(3):
                    value = grid[row+x][col+y]
                    if value not in visited:
                        return False
                    visited.remove(value)
                    rows[x] += value
                    if rows[x] > 15:
                        return False
                    cols[y] += value
                    if cols[y] > 15:
                        return False
                    if x == y:
                        neg += value
                        if neg > 15:
                            return False
                    if x+y == 2:
                        pos += value
                        if pos > 15:
                            return False

            for i in range(3):
                if rows[i] != 15:
                    return False
                if cols[i] != 15:
                    return False
            return True if neg == 15 and pos == 15 else False

        ans = 0
        for row in range(n-2):
            for col in range(m-2):
                ans += check(row, col)
        return ans


