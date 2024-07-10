#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = 0

        curr = 0
        for start, dur in customers:
            end = max(curr, start) + dur
            ans += end-start
            curr = end

        return ans / len(customers)