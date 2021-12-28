import sys
input = sys.stdin.readline
n, m = map(int, input().split())
bill = []
for i in range(n): bill.append(int(input()))
mon = [10001] * 10001
for d in bill:
    mon[d] = 1

bill.sort()

for i in range(1, 10001):
    min_val = mon[i]
    for d in bill:
        if (i - d) > 1:
            min_val = min(min_val, mon[i-d] + 1)
    mon[i] = min_val

print(mon[m])