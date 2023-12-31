# https://school.programmers.co.kr/learn/courses/30/lessons/84512 모음 사전

'''
1. 아이디어 :
    모든 조합을 만든 후, 몇번째인지 찾는다.
2. 시간복잡도 :
    O(5**5)
3. 자료구조 :
    배열
'''

def solution(word):
    word = list(word)

    words = []
    visited = set()
    add = ["A", "E", "I", "O", "U"]
    found = 0
    def dfs(string, idx):
        if idx == 6:
            return

        words.append(string)

        for a in add:
            new_string = string + a
            dfs(new_string, idx+1)

    dfs("", 0)
    return words.index("".join(word))

