# https://leetcode.com/problems/baseball-game/description/

'''
1. 아이디어 :
    - 스택을 활용하여 operation의 character 마다 확인.
2. 시간복잡도 :
    - O(n) : n은 operations의 길이
3. 자료구조 :
    - 스택
'''


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for c in operations:
            if c=="D":
                records.append(records[-1]*2)
            elif c=="C":
                records.pop()
            elif c=="+":
                records.append(records[-1]+records[-2])
            else:
                records.append(int(c))
        return sum(records)