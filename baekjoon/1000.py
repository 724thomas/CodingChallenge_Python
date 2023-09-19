# https://www.acmicpc.net/problem/1000

# nums = list(map(int, sys.stdin.readline().split()))
# num=int(sys.stdin.readline())
# h, w, n = map(int, sys.stdin.readline().split())

def prime_list(start, end):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * end
    if start <= 0:
        start = 2

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(end ** 0.5)
    for i in range(start, m + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, end, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(start, end) if sieve[i]]


print(prime_list(10, 100))
