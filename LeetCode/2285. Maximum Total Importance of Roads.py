#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n

        for [first, second] in roads:
            degrees[first] += 1
            degrees[second] += 1

        degrees.sort()
        total = 0

        for index in range(1, n + 1):
            total += degrees[index - 1] * index

        return total

