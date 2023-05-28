# https://leetcode.com/problems/top-k-frequent-elements/description/

'''
1. 아이디어 :
    Counter와 정렬을 사용한다.
2. 시간복잡도 :
    O(n) + O(nlogn) + O(n) = O(nlogn)
3. 자료구조 :
    배열, 해시맵
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        nums = sorted([[count,num] for num, count in c.items()])
        nums.sort(reverse = True)
        return [nums[i][1] for i in range(k)]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [sorted([[count,num] for num, count in Counter(nums).items()], reverse = True)[i][1] for i in range(k)]



    Coding_0523 Heap_And_Priority_Queue_And_Intervals/김우석/최원준/번
    [최원준] 5주차 Heap_And_Priority_Queue_And_Intervals 번