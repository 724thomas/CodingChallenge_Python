# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

'''
1. 아이디어 :
    1) 각 리스트의 첫번째 원소를 배열에 넣는다.
    2) 배열에서 최소값과 최대값을 구한다.
    3) 최소값을 가진 리스트의 첫번째 원소를 배열에서 제거하고, 다음 원소를 배열에 넣는다.
    4) 2)~3)을 반복한다.
    5) 배열의 최소값과 최대값의 차가 최소인 경우를 찾는다.
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    힙, 배열
'''

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        crange = float('inf')
        cmin = 0
        cmax = float('inf')
        for num in nums:
            heapq.heapify(num)

        candids = []
        for l in nums:
            candids.append(heapq.heappop(l))

        while True:
            check_min = min(candids)
            check_max = max(candids)
            if check_max - check_min < crange:
                cmin = check_min
                cmax = check_max
                crange = cmax - cmin

            idx = candids.index(check_min)
            if nums[idx] :
                candids[idx] = heapq.heappop(nums[idx])
            else:
                break


        return [cmin,cmax]