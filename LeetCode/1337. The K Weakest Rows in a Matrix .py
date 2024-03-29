# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

'''
1. 아이디어 :
    1) 최소힙을 사용해서 [병사수, 인덱스]를 저장하고 k만큼 뽑아낸다.
    2) 정렬을 사용해서 [병사수, 인덱스]를 정렬한 후, k만큼 뽑아낸다.
2. 시간복잡도 :
    1) O(n) + O(n) + O(logn) heappush를 하는 것보다 heapify가 더 빠르다(logn vs n)
        배열 만들기 + heapify + heappop
    2) O(nlogn)
        배열 만들기 + 정렬 + 인덱스 뽑아내기
3. 자료구조 :
    힙
'''


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [[sum(mat[i]),i] for i in range(len(mat))]
        heapq.heapify(power)
        return [heapq.heappop(power)[1] for i in range(k)]


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        for i in range(len(mat)):
            ans.append([sum(mat[i]),i])
        ans.sort()
        return [ans[i][1] for i in range(k)]