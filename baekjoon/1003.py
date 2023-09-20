#https://www.acmicpc.net/problem/1003
import sys
#nums = list(map(int, input().split()))
case = int(sys.stdin.readline())

for i in range(case):
    n = int(sys.stdin.readline())
    fib={}
    fib[0]=[1,0]
    fib[1]=[0,1]
    for i in range(2,n+1):
        if i not in fib:
            c0 = fib[i-1][0] + fib[i-2][0]
            c1 = fib[i-1][1] + fib[i-2][1]
            fib[i]=[c0,c1]
    print (str(fib[n][0]) + " " +str(fib[n][1]))




