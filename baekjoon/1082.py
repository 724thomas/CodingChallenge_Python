# https://www.acmicpc.net/problem/1082

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

n = int(input())
cost = list(map(int, input().split()))
m = int(input())

# print(n, cost, m)

candid = []


def bt(num, money):
    candid.append("".join(num))
    for i in range(len(cost)):
        if money >= cost[i]:
            bt(num + [str(i)], money - cost[i])


bt([], m)
candid = sorted([int(x) for x in candid[1:]])
print(candid[-1])
print(candid)
