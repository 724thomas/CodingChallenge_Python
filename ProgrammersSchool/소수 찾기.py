# https://school.programmers.co.kr/learn/courses/30/lessons/42839 소수 찾기

'''
1. 아이디어 :
    소수 리스트를 먼저 만든다.
    Counter를 이용해서, 각 소수를 만들 수 있는지 확인한다.
2. 시간복잡도 :
    O(n^2)
3. 자료구조 :
    배열, 해시맵
'''

from collections import Counter
def solution(numbers):
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

    def check_numbers(c, prime):
        prime_c = Counter(str(prime))
        for k, v in prime_c.items():
            if prime_c[k] > c[k]:
                return False
        return True

    n = sorted(list(numbers), reverse=True)
    primes = set(prime_list(0, int("".join(n))+1))

    c = Counter(numbers)
    count=0
    for n in primes:
        if check_numbers(c, n):
            count+=1
    return count





