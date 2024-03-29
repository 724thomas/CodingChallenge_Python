# https://leetcode.com/problems/find-the-town-judge/

'''
1. 아이디어 :
    해시맵으로, 믿는 사람과 믿음을 받는 사람을 저장한다.
    믿음을 받는 사람이 n-1명이고, 믿는 사람이 없는 사람이 단 한명이면 그 사람이 답이다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    해시맵
'''


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trusts = {}
        trusted = {}

        for t in trust:
            if t[0] not in trusts:
                trusts[t[0]] = set()
            trusts[t[0]].add(t[1])

            if t[1] not in trusted:
                trusted[t[1]] = set()
            trusted[t[1]].add(t[0])

        for k, v in trusted.items():
            if len(v) == n - 1 and k not in trusts:
                return k
        return -1
