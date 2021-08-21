n = int(input())

dp = []
for _ in range(n):
    temp = list(map(int, input().split()))
    dp.append(temp)


for i in range(1, n):
    m = len(dp[i])
    for k in range(m):
        if k == 0:
            dp[i][k] = dp[i][k] + dp[i - 1][k]
        elif k == (m - 1):
            dp[i][k] = dp[i][k] + dp[i - 1][k - 1]
        else:
            dp[i][k] = dp[i][k] + max(dp[i - 1][k - 1], dp[i - 1][k])

print(max(dp[n-1]))