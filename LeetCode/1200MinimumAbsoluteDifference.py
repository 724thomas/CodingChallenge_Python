#https://leetcode.com/problems/minimum-absolute-difference/

'''
1. 아이디어 :
    정렬 후 인접한 두 수의 차이를 구하고 그 중 최소값을 구한다.
2. 시간복잡도 :
    O(n*logn) + O(n) + O(n)
3. 자료구조 :
    리스트
'''


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        cmin=float('inf')
        for i in range(len(arr)-1):
            cmin=min(abs(arr[i+1]-arr[i]),cmin)
        ans=[]
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])==cmin:
                ans.append([arr[i],arr[i+1]])
        return ans
