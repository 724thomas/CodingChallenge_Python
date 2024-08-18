#

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                ans +=1
        return ans