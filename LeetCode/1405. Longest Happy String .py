# https://leetcode.com/problems/longest-happy-string/description/

'''
1. 아이디어 :
    힙을 사용할 수 있다.
    제일 많은 것부터 꺼낸 후, 꺼낸거와 앞에 두개의 char가 일치하는 경우, 두번째꺼를 꺼낸다.
    두번째가 없는 경우, break
    꺼낸거의 count를 차감한 후 다시 heap에 넣는다.
2. 시간복잡도 :
    O(nlogn)
3. 자료구조 :
    힙
'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heap.append([-a,"a"])
        if b:
            heap.append([-b,"b"])
        if c:
            heap.append([-c,"c"])
        heapq.heapify(heap)
        ans = ""

        for i in range(2):
            cmax = heapq.heappop(heap)
            ans+=cmax[1]
            cmax[0] +=1
            if cmax[0]<0:
                heapq.heappush(heap,cmax)

        while heap:
            pre1 = ans[-2]
            pre2 = ans[-1]
            temp1 = heapq.heappop(heap)
            if heap and pre1 == pre2 == temp1[1]:
                temp2 = heapq.heappop(heap)
                ans+=temp2[1]
                temp2[0]+=1
                if temp2[0]<0:
                    heapq.heappush(heap,temp2)
                heapq.heappush(heap,temp1)
            elif pre1==pre2==temp1[1]:
                break
            else:
                ans+=temp1[1]
                temp1[0]+=1
                if temp1[0]<0:
                    heapq.heappush(heap,temp1)
        return ans
