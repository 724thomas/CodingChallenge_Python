#https://leetcode.com/problems/longest-turbulent-subarray/description/

'''
1. 아이디어 :
    sliding window로 풀 수 있다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    배열
'''

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        cmax, prev = 1, ""

        while r< len(arr):
            if arr[r-1] > arr[r] and prev!= ">":
                cmax = max(cmax, r-l+1)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev!= "<":
                cmax = max(cmax, r-l+1)
                r += 1
                prev = "<"
            else:
                if arr[r-1] == arr[r]:
                    r+=1
                l = r - 1
                prev = ""

        return cmax



