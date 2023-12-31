# https://school.programmers.co.kr/learn/courses/30/lessons/87946 피로도

'''
1. 아이디어 :
    백트래킹
2. 시간복잡도 :
    O(2^n)
3. 자료구조 :
    해시셋
'''


def solution(k, dungeons):
    def backtrack(fat, count):
        ans[0] = max(ans[0], count)

        for i in range(len(dungeons)):
            if fat >= dungeons[i][0] and i not in visited:
                visited.add(i)
                backtrack(fat - dungeons[i][1], count + 1)
                visited.remove(i)

    visited = set()
    ans = [0]
    backtrack(k, 0)
    return ans[0]
