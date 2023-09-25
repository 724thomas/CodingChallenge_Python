# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

string = input()
alpha = [0] * 26
for c in string:
    alpha[ord(c) - 65] += 1
ans = ""
for i in range(len(alpha)):
    ans += chr(i + 65) * (alpha[i] // 2)
    alpha[i] %= 2
if len(string) % 2 == 0: # Even
    if sum(alpha) == 0:
        print(ans + ans[::-1])
    else:
        print("I'm Sorry Hansoo")
else: # Odd
    if sum(alpha) == 1:
        print(ans + chr(alpha.index(1) + 65) + ans[::-1])
    else:
        print("I'm Sorry Hansoo")