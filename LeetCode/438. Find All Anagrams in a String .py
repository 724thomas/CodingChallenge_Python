# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

'''
1. 아이디어 :
    전형적인 슬라이딩 윈도우 문제다.
    c 해시맵에 p의 char와 갯수를 저장
    check에 p의 길이만큼의 char와 갯수를 저장.
    s[left]와 s[right]를 하나씩 옮기면서 뺴고, 더한다.
    해시맵 갯수가 check와 같으면 left를 저장.
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    해시맵
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c, check, left, right, ans = Counter(p), Counter(s[:len(p)]), 0, len(p), []

        while right<len(s):
            if check == c:
                ans.append(left)

            check[s[left]]-=1
            if s[right] not in check:
                check[s[right]] = 1
            else:
                check[s[right]] += 1

            left+=1
            right+=1

        if check==c:
            ans.append(left)
        return ans