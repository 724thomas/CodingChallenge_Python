# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(N)
3. 자료구조 :
    배열
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        while i<len(letters):
            if letters[i] > target:
                return letters [i]
            i += 1
        return letters[0]