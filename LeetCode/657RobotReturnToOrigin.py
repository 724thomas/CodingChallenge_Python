#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R")