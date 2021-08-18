n = int(input())
stages = list(map(int, input()))

total = len(stages)

stages.sort()

# 계수 정렬 용 배열
ary = [0] * (n + 2)

# 실패율 저장용 배열
fail = []

# 계수정렬 사용
for i in range(total):
    ary[stages[i]] += 1

for i in range(1, n + 1):
    if ary[i] > 0:
        fail.append((ary[i] / total, i))
        total -= ary[i]
    else:
        fail.append((0, i))

fail.sort(reverse=True, key=lambda x: (x[0], -x[1]))

new_ary = []
for i in range(n):
    new_ary.append(fail[i][1])

print(new_ary)
