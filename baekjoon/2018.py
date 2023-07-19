# https://www.acmicpc.net/problem/2018

'''
1. 아이디어 :
    1) 투 포인터. 합이 같으면 왼, 오른쪽 포인터 이동. 작으면 왼쪽, 크면 오른쪽 이동.
    2) count로 나눠질 수 있는지 확인 후, n에 count를 차감, count에 1을 더하여 n이 0이하가 될때까지 확인
2. 시간복잡도 :
    1) O(n)
    2) O(n)
3. 자료구조 :
    1) -
    2) -
'''

n = int(input())

ans, left, right, total = 0, 1, 1, 1

while right != n + 1:
    if total == n:
        ans += 1
        right += 1
        total = total + right - left
        left += 1
    elif total < n:
        right += 1
        total += right
    elif total > n:
        total -= left
        left += 1
print(ans)


n = int(input())

ans = 0
count = 1

while True:
    if n % count == 0:
        ans += 1
    n -= count
    count += 1

    if n <= 0:
        break

print(ans)
