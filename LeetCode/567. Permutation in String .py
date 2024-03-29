# https://leetcode.com/problems/permutation-in-string/description/

'''
1. 아이디어 :
    1, 슬라이딩 윈도우와 해시맵을 사용
    2. 투 포인터를 사용해서 해시맵을 체크하는 과정을 건너뛴다.
2. 시간복잡도 :
    1. O(26*n) = O(n)
    2. O(n)
3. 자료구조 :
    1. 해시맵
    2. 배열
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        l = 0
        r = len(s1)-1
        counter1 = Counter(s1)
        count = {}



        def check(counter, count):
            for k,v in counter.items():
                if k not in count or count[k] != v:
                    return False
            return True

        for i in range(len(s1)):
            count[s2[i]] = 1 + count.get(s2[i],0)
        if count == counter1:
            return True

        while r<len(s2)-1:
            count[s2[l]]-=1
            l+=1
            r+=1
            count[s2[r]] = 1+count.get(s2[r],0)
            if check(counter1, count):
                return True
        return False



'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i])- ord('a')] +=1
            s2Count[ord(s2[i])- ord('a')] +=1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index]+=1
            if s1Count[index] == s2Count[index]:
                matches +=1
            if s1Count[index] + 1 == s2Count[index]:
                matches -=1

            index = ord(s2[l]) - ord('a')
            s2Count[index]-=1
            if s1Count[index] == s2Count[index]:
                matches +=1
            if s1Count[index] - 1 == s2Count[index]:
                matches -=1
            l+=1
        return matches == 26

        
'''