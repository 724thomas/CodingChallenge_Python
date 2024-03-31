#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(  )
3. 자료구조 :

'''


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for s in strs:
            words["".join(sorted(s))].append(s)

        return [v for k,v in words.items()]

