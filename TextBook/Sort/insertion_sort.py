# 선택 정렬 -> 매번 가장 작은 것을 선택
n = int(input())

ary = list(map(int, input().split()))

# 오름차순
for i in range(n):
    min_pos = i
    for j in range(i + 1, n):
        if ary[min_pos] > ary[j]:
            ary[min_pos], ary[j] = ary[j], ary[min_pos]
            min_pos = j

print(ary)
