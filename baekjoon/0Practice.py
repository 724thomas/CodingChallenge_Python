#

'''
1. 아이디어 :

2. 시간복잡도 :

3. 자료구조 :

'''

def prime_list(start, end):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * end
    if start <= 0:
        start = 2

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(end ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, end, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(start, end) if sieve[i]]


import sys
input = sys.stdin.readline
cases = int(input())
prime_table = prime_list(0, 10 ** 7)
temp_table = prime_table.copy()
for _ in range(cases):
    n = int(input())
    lengths = list(map(int, input().split()))

    for j in range(n):
        temp_list=[]
        length = lengths[j]
        temp_total = 0
        for i in range(length):
            temp_total += prime_table[i]
        lp = 0
        rp = lp + length
        while rp < len(prime_table) and temp_total <= 10 **7:
            if temp_total in prime_table:
                temp_list.append(temp_total)
            temp_total -= prime_table[lp]
            lp += 1
            temp_total += prime_table[rp]
            rp += 1
        # print(sorted(temp_list))
        temp_table = list(set(temp_table) & set(temp_list))
    print("Scenario {}:".format(_+1))
    #if len(temp_table)==0:
    #    assert False
    print(sorted(temp_table)[0])