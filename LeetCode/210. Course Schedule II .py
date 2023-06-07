# https://leetcode.com/problems/course-schedule-ii/description/

'''
1. 아이디어 :
    1) 그래프를 만든다. 그래프는 해시맵으로 구현한다. key는 노드, value는 노드와 연결된 노드들이다.
    2) in_degree 배열을 만든다. in_degree[i]는 i번째 노드로 들어오는 간선의 개수이다.
    3) in_degree[i]가 0인 노드들을 큐에 넣는다.
    4) 큐에서 노드를 하나씩 빼면서, 그 노드와 연결된 노드들의 in_degree를 1씩 줄인다.
    5) in_degree가 0이 된 노드들을 큐에 넣는다.
    6) 큐가 빌 때까지 반복한다.
    7) 만약 result의 길이가 numCourses보다 작다면, 사이클이 존재한다는 뜻이므로 빈 배열을 리턴한다.
2. 시간복잡도 :
    O(N) * O(1)
3. 자료구조 :
    해시맵, 배열
'''

from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        #print(graph)

        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            in_degree[course] += 1
        #print(in_degree)

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        #print(queue)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < numCourses:
            return []

        return result