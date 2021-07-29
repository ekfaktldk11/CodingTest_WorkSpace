# 정수 N을 입력받기
n, m = map(int, input().split())

n_ary = []
for i in range(n):
    n_ary.append(int(input()))

n_ary.sort()

d = [10001] * (m + 1)
d[0] = 0

# i - k 원을 만들 수 있는 경우 & 그럴 수 없는 경우를 나눠서 탑 다운

for i in range(n):
    for j in range(n_ary[i], m + 1):
        if d[j - n_ary[i]] != 10001:
            d[j] = min(d[j], d[j - n_ary[i]] + 1)

if(d[m] == 10001):
    print(-1)
else:
    print(d[m])