# 정수 N을 입력받기
n, m = map(int, input().split())

n_ary = list(map(int, input().split()))

n_ary.sort()

d = [10001] * (m + 1)
d[0] = 0

# i - k 원을 만들 수 있는 경우 & 그럴 수 없는 경우를 나눠서 탑 다운

for i in range(n):
    for j in range(1, m + 1):
        if j % n_ary[i] == 0:
            d[j] = min(d[j], d[j - n_ary[i]] + 1)