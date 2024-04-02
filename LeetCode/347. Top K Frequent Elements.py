#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = sorted([ (v,k) for k,v in Counter(nums).items() ], reverse=True)
        return [freq[i][1] for i in range(k)]