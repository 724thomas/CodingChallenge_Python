# https://leetcode.com/problems/number-of-provinces/description/

'''
1. 아이디어 :
    해시맵을 만들어서 각 키마다 bfs를 돌린다.
    visited에 없을떄마다 count 증가
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시셋, 해시맵
'''

from collections import defaultdict, deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        hmap = {}
        length = len(isConnected)
        for i in range(length):
            for j in range(length):
                if i+1 not in hmap:
                    hmap[i+1] = set()
                if j+1 not in hmap:
                    hmap[j+1] = set()
                if i!=j and isConnected[i][j] == 1:
                    hmap[i+1].add(j+1)
                    hmap[j+1].add(i+1)

        visited = set()
        for key, val in hmap.items():
            if key not in visited:
                queue = deque()
                queue.append(key)
                visited.add(key)
                count+=1
                while queue:
                    city = queue.popleft()
                    for dest in hmap[city]:
                        if dest not in visited:
                            visited.add(dest)
                            queue.append(dest)
        return count


