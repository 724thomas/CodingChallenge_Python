# https://leetcode.com/problems/matchsticks-to-square/description/

'''
1. 아이디어 :
    4 면을 똑같이 채우면 된다.
2. 시간복잡도 :
    O( 4**n )
3. 자료구조 :
    배열
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        length = sum(matchsticks)//4
        sides = [0] * 4

        if sum(matchsticks) /4 != length:
            return False

        matchsticks.sort(reverse=True)

        def backtrack(idx):
            if idx == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[idx] <= length:
                    sides[i] += matchsticks[idx]
                    if backtrack(idx+1):
                        return True
                    sides[i] -= matchsticks[idx]
            return False

        return backtrack(0)
