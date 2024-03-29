# https://leetcode.com/problems/swim-in-rising-water/description/

'''
1. 아이디어 :
    1) 최소힙을 사용하여 방문 가능한 노드들을 저장한다.
    2) 방문 가능한 노드들 중에 가장 낮은 높이의 노드를 방문한다.
    3) 1)~2)를 반복하고, 목적지에 도착하면 방문했던 노드들중의 최대 높이를 반환한다.
2. 시간복잡도 :
    O(n^2) * O(logN) = O(n^2logN) :
    grid를 방문하는 수 * heappush, heappop
3. 자료구조 :
    최소 힙, 해시셋, 배열
'''

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        max_height = 0

        while heap:
            height, row, col = heapq.heappop(heap)
            max_height = max(max_height, height)

            if row == n - 1 and col == n - 1:
                return max_height

            visited.add((row, col))

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy

                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    heapq.heappush(heap, (grid[new_row][new_col], new_row, new_col))
                    visited.add((new_row, new_col))


Coding_0523 Heap_And_Priority_Queue_And_Intervals/김우석/최원준/5번
[최원준] 5주차 Heap_And_Priority_Queue_And_Intervals 5번