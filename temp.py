import sys
# 채택된 식량 창고 check
d = [0] * 100

# 식량 창고 수
n = int(input())

# 창고 마다의 식량 수
n_ary = list(map(int, sys.stdin.readline().split()))
n_ary.append(0)
n_ary.append(0)
n_ary.append(0)
n_ary.append(0)
n_ary.append(0)
n_ary.append(0)


print(n_ary)

for i in range(0, n + 2, 2):
    r1 = n_ary[i] + max(n_ary[i + 2], n_ary[i + 3])
    r2 = n_ary[i + 1] + max(n_ary[i + 3], n_ary[i + 4])
    if (r1 >= r2): d[i] = 1
    else: d[i + 1] = 1

sum = 0
for i in range(n):
    if d[i] == 1: sum += n_ary[i]
print(d)
print(sum)