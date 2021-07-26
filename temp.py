import sys

# 부품 개수
n = int(input())
n_ary = set(map(int, sys.stdin.readline().split()))
# n_ary = set(map(int, sys.stdin.readline().split()))

print(n_ary)
# n_ary.sort()

# 주문
m = int(input())
m_ary = list(map(int, sys.stdin.readline().split()))


for i in range(m):
    if m_ary[i] in n_ary:
        print('yes', end=' ')
    else:
        print('no', end=' ')