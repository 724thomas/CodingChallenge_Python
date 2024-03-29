# https://school.programmers.co.kr/learn/courses/30/lessons/12906

'''
1. 아이디어 :
    포인터 2개를 두고 같으면 넘어가고, 다르면 append
2. 시간복잡도 :
    O(n)
3. 자료구조 :
    배열
'''

def solution(arr):
    ans = [arr[0]]
    base = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != base:
            base = arr[i]
            ans.append(base)
    return ans