# https://www.acmicpc.net/problem/5597 과제 안 내신분..?

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

students = set()
for i in range(30):
    students.add(i + 1)
print(students)
for _ in range(28):
    students.remove(int(input().rstrip()))
a, b = list(students)
if a < b:
    print(a)
    print(b)
else:
    print(b)
    print(a)
