#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            new = arr[i]
            arr[i] = biggest
            biggest = max(biggest, new)
        return arr