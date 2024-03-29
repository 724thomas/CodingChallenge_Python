# https://www.acmicpc.net/problem/7512

'''
1. 아이디어 :
    1) (시간초과)에라토스테네스의 체로 소수를 구한다.
    해시맵을 만들어서 연속돼는 n의 합을 슬라이딩 윈도우로 구하고,
    소수인지 확인한다음, 해시맵에 넣는다. value가 m인 첫번째 key를 출력한다.
    2) (틀림) 에라토스테네스의 체를 너무 많이 연산했더니 시간초과가 난다. 각 n에 대해 1000가지만 셋에 저장해봤다.
    3) 1000이상으로 가면 시간초과, 그 이하는 답이 안나온다.
    다른 방법으로 에라토스테네스의 체로 소수를 10^4까지 구하고, 연속되는 n에 대해 set을 10^4개 만들어서 저장한다.
    슬라이딩 윈도우로, 연속되는 n의 합의 모든 수를 소수이면 set[n]에 다 넣는다.
    입력되는 n들에 대해, set들의 교집합을 구한다
2. 시간복잡도 :
    1) O(10**7) * O(10**7) + O(t) * O(m) * O(10**7) = max( O(10**14), O(t) * O(m) * O(10**7) )
    2) O(10**4) * O(10**4) + O(10**4) * O(10**4) + O(t) * O(m) = O(10**8)
    - 에라토스테네스의 체 + 소수들 * 슬라이딩 윈도우 + 테스트케이스 * m
3. 자료구조 :
    1) 에라토스테네스의 체, 해시맵
    1) 에라토스테네스의 체, 배열, set
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
n = 10 ** 7
primes = prime_list(0, n)
primes_set = set(primes)
n_primes = [set() for _ in range(10 ** 4 + 1)]
for n in range(1, 10 ** 4 + 1):
    n_prime = sum(primes[:n])
    if n_prime in primes_set:
        n_primes[n].add(n_prime)
    for i in range(n, len(primes)):
        n_prime += primes[i] - primes[i - n]
        if n_prime >= 10 ** 7:
            break
        if n_prime in primes_set:
            n_primes[n].add(n_prime)
t = int(sys.stdin.readline())
for tests in range(1, t + 1):
    m = int(input())
    nums = [int(x) for x in input().split()]
    answer = primes_set.copy()
    for j in range(m):
        answer &= n_primes[nums[j]]
    print("Scenario %d:" % tests)
    print(min(answer))
    print()



# 1)
# import sys
# alist = [1,2,3,4]
# blist = [2,4]
# input = sys.stdin.readline
# cases = int(input())
# prime_table = prime_list(0, 10 ** 7)
# temp_table = prime_table.copy()
# for _ in range(cases):
#     n = int(input())
#     lengths = list(map(int, input().split()))
#
#     for j in range(n):
#         temp_list=[]
#         length = lengths[j]
#         temp_total = 0
#         for i in range(length):
#             temp_total += prime_table[i]
#         lp = 0
#         rp = lp + length
#         while rp < len(prime_table) and temp_total<= 10 **4:
#             if temp_total in prime_table:
#                 temp_list.append(temp_total)
#             temp_total -= prime_table[lp]
#             lp += 1
#             temp_total += prime_table[rp]
#             rp += 1
#         # print(sorted(temp_list))
#         temp_table = list(set(temp_table) & set(temp_list))
#     print("Scenario {}:".format(_+1))
#     #if len(temp_table)==0:
#     #    assert False
#     print(sorted(temp_table)[0])