#

'''
1. 아이디어 :
ㅤㅤ슬라이딩 윈도우와 해시맵으로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
ㅤㅤ해시맵
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])

        l = 0
        r = len(s1)

        while r < len(s2):
            if c1 == c2:
                return True

            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                del c2[s2[l]]

            c2[s2[r]] += 1
            l+=1
            r+=1

        return False if c1 != c2 else True