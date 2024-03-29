# https://leetcode.com/problems/top-k-frequent-words/description/

'''
1. 아이디어 :
    1)  Counter를 이용하여 각 단어의 빈도수를 구한다.
        최대 500단어가 들어가므로, 빈도수를 1500에서 빼서 문자열 앞에 붙여준다.
        이렇게 하면, 빈도수가 높은 단어가 앞으로 오게 된다.
        문자열을 정렬하고, 앞에서부터 k개를 추출한다.
2. 시간복잡도 :
    1) O(n) + O(n) + O(nlogn) + O(k)
        Counter + for문 + 정렬 + 추출
3. 자료구조 :
    1) 해시맵
'''


from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        temp = []
        for key,val in c.items():
            temp.append(str(1500-val) + key)
        temp.sort()
        return [temp[x][4:] for x in range(k)]