#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = {str(i):str(mapping[i]) for i in range(len(mapping))}

        for i, n in enumerate(nums):
            temp = list(str(n))
            for j, c in enumerate(temp):
                temp[j] = mapping[c]
            temp = int("".join(temp))
            nums[i] = [nums[i], temp]
        nums.sort(key=lambda x: x[1])
        return [num[0] for num in nums]