#https://leetcode.com/problems/detect-capital/description/

'''
1. 아이디어 :
    대문자로 변환한 문자열과 비교하면 된다.
2. 시간복잡도 :
    O(1)
3. 자료구조 :
    문자열
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s1=word.upper()
        s2=word.lower()
        s3=word.capitalize()

        return word==s1 or word==s2 or word==s3