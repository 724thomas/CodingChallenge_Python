#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def calc_cost(x1,y1, x2,y2):
            return abs(x1-x2) + abs(y1-y2)

        edges = defaultdict(list)
        for x1, y1, x2, y2, cost in specialRoads:
            if calc_cost(x1, y1, x2, y2) > cost:
                edges[(x1, y1)].append((cost, x2, y2))

        min_heap = [(0, start[0], start[1])]
        visited = {}

        while min_heap:
            curr_cost, curr_x, curr_y = heapq.heappop(min_heap)
            # 현재 위치가 타겟 위치라면, 최종 비용을 반환
            if curr_x == target[0] and curr_y == target[1]:
                return curr_cost

            # 이미 방문한 노드이면 continue
            if (curr_x, curr_y) in visited:
                continue
            visited[(curr_x, curr_y)] = curr_cost

            # 현재 노드에서 특수 도로를 타고 나왔을때
            if (curr_x, curr_y) in edges:
                for dest_cost, dest_x, dest_y in edges[(curr_x, curr_y)]:
                    if (dest_x, dest_y) not in visited or curr_cost + dest_cost < visited[(dest_x, dest_y)]:
                        heapq.heappush(min_heap, (curr_cost + dest_cost, dest_x, dest_y))

            # 현재 노드에서 특수 도로까지 갔을때
            for dest_x, dest_y in edges:
                if (dest_x, dest_y) not in visited:
                    heapq.heappush(min_heap, (curr_cost + calc_cost(curr_x, curr_y, dest_x, dest_y), dest_x, dest_y))

            # 타겟까지 바로 가는 경로를 추가
            heapq.heappush(min_heap, (curr_cost + calc_cost(curr_x, curr_y, target[0], target[1]), target[0], target[1]))














        return