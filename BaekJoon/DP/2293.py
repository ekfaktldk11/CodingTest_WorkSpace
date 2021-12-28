'''
- 동전 1
- https://www.acmicpc.net/problem/2293
'''

n, k = map(int, input().split())
c = []
dp = [0] * (k + 1)
dp[0] = 1
for i in range(n):
    c.append(int(input()))
for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])

'''
# 결론
- 입력예제를 구하기 위해 손으로 풀어보다 감을 익혀야 함
- 예를들어 n = 3, k = 10 이고, 각 화폐가 1, 2, 5 라면
- 각 화폐 단위마다 모든 10원까지 만들 수 있는 금액을 나열하다 보면 일정의 규칙을 찾을 수 있음
- 그 규칙을 코드로 옮기면 됨
- 출처 : https://pacific-ocean.tistory.com/200
'''