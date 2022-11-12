# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

'''
1. 아이디어 :
    짝수, 홀수 힙을 만들어서, 짝수는 가장 큰 수를, 홀수는 가장 작은 수를 뽑아서 문자열에 붙인다.
2. 시간복잡도 :
    O(N * logN)
3. 자료구조 :
    힙, 문자열
'''

class Solution:
    def largestInteger(self, num: int) -> int:
        nums = str(num)
        odd_heap = []
        even_heap = []
        for i in range(len(nums)):
            num = int(nums[i])
            if num %2 :
                heapq.heappush(odd_heap,-num)
            else:
                heapq.heappush(even_heap,-num)

        ans = ""
        for i in range(len(nums)):
            if int(nums[i]) %2 :
                ans+= str(-heapq.heappop(odd_heap))
            else:
                ans+= str(-heapq.heappop(even_heap))
        return int(ans)
