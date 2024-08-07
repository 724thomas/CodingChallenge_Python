#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        temp = []
        for k, v in counter.items():
            temp.append((k, v))
        temp.sort(key = lambda x : (x[1], -x[0]))
        ans = []
        for num, count in temp:
            for _ in range(count):
                ans.append(num)
        return ans
