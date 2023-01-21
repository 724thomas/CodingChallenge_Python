#https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                leftc= i==0 or flowerbed[i-1]==0
                rightc= i==len(flowerbed)-1 or flowerbed[i+1]==0
                print(i, leftc, rightc)
                if leftc and rightc:
                    flowerbed[i]=1
                    i+=1
                    n-=1
            if n<=0:
                return True
        return False