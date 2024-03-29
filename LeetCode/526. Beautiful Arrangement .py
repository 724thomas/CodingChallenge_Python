# https://leetcode.com/problems/beautiful-arrangement/description/

'''
1. 아이디어 :
    백트래킹 사용. 방문한 숫자를 set에 저장하고, 인덱스를 매개변수로 재귀호출
2. 시간복잡도 :
    O(n!)
3. 자료구조 :
    해시셋
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0

        def backtrack(idx, temp_set):
            if len(temp_set) == n:
                self.count +=1
                return
            for i in range(1, n+1):
                if i not in temp_set and (i % idx == 0 or idx % i ==0) :
                    temp_set.add(i)
                    backtrack(idx+1, temp_set)
                    temp_set.remove(i)

        backtrack(1,set())
        return self.count