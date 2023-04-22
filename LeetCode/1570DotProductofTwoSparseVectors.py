#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''


class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr=nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans=0
        for i in range(len(self.arr)):
            ans+=self.arr[i]*vec.arr[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)