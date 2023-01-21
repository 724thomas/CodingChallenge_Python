#https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            temp=image[i][::-1]
            for j in range(len(temp)):
                temp[j]=(temp[j]*-1)+1
            image[i]=temp
        print(image)
        return image