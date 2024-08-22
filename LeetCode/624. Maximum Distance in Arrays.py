#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import heapq
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # print(*arrays, sep='\n')
        n = len(arrays)
        ans = -float('inf')
        mins = []
        maxs = []
        for a in arrays:
            mins.append(a[0])
            maxs.append(a[-1])
        mins.sort()
        maxs.sort()

        for a in arrays:
            amin = a[0]
            amax = a[-1]

            if amax == maxs[-1]:
                ans = max(ans, abs(amin- maxs[-2]))
            else:
                ans = max(ans, abs(amin- maxs[-1]))
            if amin == maxs[0]:
                ans = max(ans, abs(amin - mins[1]))
            else:
                ans = max(ans, abs(amin - mins[0]))

        return ans


        min_heap = []
        max_heap = []
        ans = -float('inf')

        for a in arrays:
            heapq.heappush(min_heap, a[0])
            heapq.heappush(max_heap, -a[-1])

        for a in arrays:
            amin = a[0]
            amax = a[-1]

            temp = ''
            if max_heap[0] == -amax:
                temp = heapq.heappop(max_heap)
            ans = max(ans, abs(amin + max_heap[0]))
            if temp!= '':
                heapq.heappush(max_heap, temp)

            temp = ''
            if min_heap[0] == amin:
                temp = heapq.heappop(min_heap)
            ans = max(ans, abs(amax - min_heap[0]))
            if temp != '':
                heapq.heappush(min_heap, temp)
        return ans