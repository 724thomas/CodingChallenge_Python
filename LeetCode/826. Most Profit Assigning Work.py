#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import deque
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        pd = sorted([(profit[i], difficulty[i]) for i in range(len(profit))], key = lambda x: (-x[0], x[1]))
        print(pd)
        ans = 0
        for profit, difficulty in pd:
            while worker:
                if difficulty <= worker[-1]:
                    worker.pop()
                    ans += profit
                else:
                    break
        return ans
