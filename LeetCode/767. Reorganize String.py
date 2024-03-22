#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, S):
        ans = []
        c = Counter(S)
        chars = [(-value,key) for key,value in c.items()]
        heapq.heapify(chars)

        temp = [0, '']
        while chars:
            val, key = heapq.heappop(chars)
            ans += [key]
            if temp[0] < 0:
                heapq.heappush(chars, (temp[0], temp[1]))
            val += 1
            temp = [val, key]

        ans = ''.join(ans)

        return "" if len(ans) != len(S) else ans
