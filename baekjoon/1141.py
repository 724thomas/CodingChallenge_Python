# https://www.acmicpc.net/problem/1141

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

n = int(input())
words = []
for _ in range(n):
    words.append(input())

words.sort(key=lambda x: len(x))
print(words)

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        index = -1
        try:
            index = words[j].index(words[i])
        except:
            j = len(words)
        print(index)
