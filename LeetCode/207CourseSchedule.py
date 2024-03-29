#https://leetcode.com/problems/course-schedule/description/

'''
1. 아이디어 :
    DFS로 풀 수 있다.
2. 시간복잡도 :
    O(n + e)
    n: number of courses , e: edges
3. 자료구조 :
    해시셋, 해시맵, 배열
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        print(courses)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if courses[course] == []:
                return True

            visited.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            courses[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True