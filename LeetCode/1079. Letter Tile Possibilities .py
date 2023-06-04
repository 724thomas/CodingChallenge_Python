# https://leetcode.com/problems/letter-tile-possibilities/description/

'''
1. 아이디어 :
    해시셋을 이용하여 사용 가능한 char을 추적하고, 백트래킹을 이용하여, 사용된 char의 숫자를 줄여가며, 가능한 모든 경우의 수를 구하고,
    visited에 저장하여 중복을 제거한다. 마지막으로 ""을 제거.
2. 시간복잡도 :
    O(N!)
3. 자료구조 :
    해시셋
'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        visited = set()
        chars = {}
        for c in tiles:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c]+=1

        def backtrack(s):
            if s not in visited:
                visited.add(s)

            if not chars:
                return

            for k,v in chars.items():
                if chars[k] != 0:
                    chars[k] -=1
                    backtrack(s+k)
                    chars[k] +=1

        backtrack("")
        return len(visited)-1
