# https://school.programmers.co.kr/learn/courses/30/lessons/43162 네트워크

'''
1. 아이디어 :
    queue를 사용할 수 있다.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵, 해시셋, 배열
'''

from collections import defaultdict
from collections import deque


def solution(n, computers):
    hmap = defaultdict(list)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                hmap[i].append(j)

    visited = set()
    count = 0
    for i in range(len(computers)):
        if i not in visited:
            count += 1
            visited.add(i)
            queue = deque()
            queue.append(i)
            while queue:
                start = queue.popleft()
                for dest in hmap[start]:
                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)
    return count
