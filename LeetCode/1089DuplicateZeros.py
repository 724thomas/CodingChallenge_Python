#https://leetcode.com/problems/duplicate-zeros/

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count0=arr.count(0)
        temp=[]
        for i in range(len(arr)):
            temp.append(arr[i])
            if arr[i]==0:
                temp.append(0)
        print(temp)
        for i in range(len(arr)):
            arr[i]=temp[i]