# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

'''
1. 아이디어 :
    target의 아스키코드보다 큰 문자를 찾으면 된다. 없으면 첫번째 문자가 답이다.
2. 시간복잡도 :
    O(N)
3. 자료구조 :
    문자열
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in letters:
            if ord(target)<ord(l):
                return l
        return letters[0]