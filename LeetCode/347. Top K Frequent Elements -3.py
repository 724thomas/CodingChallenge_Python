# https://leetcode.com/problems/top-k-frequent-elements/description/

'''
1. 아이디어 :
    k,v 값으로 정렬
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x2 for x1, x2 in sorted([[v,k] for k,v in Counter(nums).items()], reverse=True)[:k]]
