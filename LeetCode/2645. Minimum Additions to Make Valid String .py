# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

'''
1. 아이디어 :
    abc, ab/bc/ac를 각 '0' 과 '1' 로 치환한다
    0 이면 count에 0을, 1이면 count에 1을, 나머지는 count에 2를 더한다
2. 시간복잡도 :
    O(n*5) = O(n)
3. 자료구조 :
    문자열
'''


class Solution:
    def addMinimum(self, word: str) -> int:
        count = 0
        while 'abc' in word:
            word = word.replace('abc', '0')
        while 'ab' in word:
            word = word.replace('ab', "1")
        while 'bc' in word:
            word = word.replace('bc', '1')
        while 'ac' in word:
            word = word.replace('ac', '1')
        for c in word:
            if c == '0':
                pass
            elif c == "1":
                count += 1
            else:
                count += 2
        return count
