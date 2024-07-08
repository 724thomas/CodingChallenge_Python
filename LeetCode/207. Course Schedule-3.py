#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses  = defaultdict(list)

        for p1, p2 in prerequisites:
            courses[p1].append(p2)

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