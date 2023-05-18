# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

'''
1. 아이디어 :
    이진탐색으로 풀었다.
    arr2를 정렬 후, arr1의 원소를 하나씩 꺼내고,
    arr2에서 이진탐색으로 arr1의 원소와 가장 가까운 원소를 찾는다.
    그 원소와의 차이가 d보다 작거나 같으면 count를 하나 줄인다.
2. 시간복잡도 :
    O(NlogN)
3. 자료구조 :
    배열
'''

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count=len(arr1)

        for num in arr1:
            start = 0
            end = len(arr2) - 1

            while start <= end:
                mid = (start+end)//2
                if abs(num-arr2[mid]) <= d:
                    count-=1
                    break
                elif num > arr2[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return count

