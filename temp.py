n = int(input())
ary = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n

for i in range(n):
    ary[i] -= b
    if ary[i] > 0:
        q, r = divmod(ary[i], c)
        if r > 0: answer += (q + 1)
        else: answer += q

print(answer)