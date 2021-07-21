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

"""
- 선택 정렬은 N - 1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
- 또한 매번 가장 작은 수를 찾기 위해서 비교 연산을 수행
- N + (N - 1) + (N + 2) + ... + 2 -> N * (N + 1)/2 : O(N^2) for Best, Avg, Worst case
"""