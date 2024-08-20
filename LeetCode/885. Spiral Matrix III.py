#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = {0: (0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}

        pos = [rStart, cStart]
        visit_left = rows * cols-1
        ans = [pos.copy()]
        dir = 0
        rounds = 1
        while visit_left:
            for _ in range(2):
                dx, dy = dirs[dir]
                for i in range(rounds):
                    pos[0] += dx
                    pos[1] += dy
                    if 0<=pos[0]<rows and 0<=pos[1]<cols:
                        visit_left -= 1
                        ans.append(pos.copy())
                dir = (dir + 1) % 4
            rounds += 1
        return ans


