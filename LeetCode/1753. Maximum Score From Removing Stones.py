# https://leetcode.com/problems/maximum-score-from-removing-stones/

'''
1. 아이디어 :
    a,b,c의 최소값 두개를 더한 것과, a+b+c의 절반을 비교해서 작은 것을 리턴하면 된다.
2. 시간복잡도 :
    O(1)
    원래 Heappush, Heappop은 logN인데, N이 상수이므로 O(1) 이다.
3. 자료구조 :
    힙
'''


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        #if a>b:
        #    a,b = b,a
        #if b>c:
        #    b,c = c,b
        #if a>c:
        #    a,c = c,a
        #return min(a+b,(a+b+c)//2)

        min_heap = []
        heapq.heappush(min_heap,a)
        heapq.heappush(min_heap,b)
        heapq.heappush(min_heap,c)
        left = 0
        total = 0
        cmin = heapq.heappop(min_heap)
        left += cmin
        total += cmin
        cmin = heapq.heappop(min_heap)
        left += cmin
        total += cmin
        cmin = heapq.heappop(min_heap)
        total += cmin
        return min(left,total//2)