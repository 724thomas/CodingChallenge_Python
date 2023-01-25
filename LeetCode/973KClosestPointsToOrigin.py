# https://leetcode.com/problems/k-closest-points-to-origin/description/

'''
1. 아이디어 :
    1)  heapq를 이용하여, distance, [x,y]를 배열에 저장한 후, heapify를 통해 heapq로 변환한다.
        ans배열을 만들고, k번만큼 heappop를 실행하여 append.
2. 시간복잡도 :
    1)  O(logN)
3. 자료구조 :
    1   우선순위큐
'''


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_distance = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = (x-0)**2 + (y-0)**2
            point_distance.append((distance, [x,y]))
        heapq.heapify(point_distance)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(point_distance)[1])
        return ans