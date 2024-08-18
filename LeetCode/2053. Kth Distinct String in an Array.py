#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = [k for k,v in Counter(arr).items() if v == 1]
        return distinct[k-1] if len(distinct) >= k else ""
