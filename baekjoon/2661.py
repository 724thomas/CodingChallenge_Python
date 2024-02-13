# https://www.acmicpc.net/problem/2661

'''
1. 아이디어 :
    백트래킹 사용
    check 메소드로 확인한다.
    check 메소드는 뒤에서부터 접두사들을 비교하여 같은 접두사가 있으면 False를 반환한다.
    뒤에서부터 접두사를 비교하는 이유는 뒤에서부터 비교하면 더 빨리 같은 접두사가 있는지 확인할 수 있기 때문이다.
    하나씩 추가되면서 비교하기때문에 앞 부분은 이미 확인한 것이기 때문에 뒤에서부터 비교하면 된다.
2. 시간복잡도 :
    O( 3**n )
3. 자료구조 :
    문자열
'''
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def check(num):
    length = len(num)
    for i in range(1, length//2+1):
        if num[-i:] == num[-2*i:-i]:
            return False
    return True

def backtrack(idx, num):
    if not check(num):
        return
    if idx == n:
        print(num)
        exit()
    for i in range(1, 4):
        num += str(i)
        backtrack(idx+1, num)
        num = num[:-1]

n = int(input().rstrip())
backtrack(0, "")