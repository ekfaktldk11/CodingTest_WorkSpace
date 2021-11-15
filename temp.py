n = int(input())
num = n;k = 0;total9 = 0;tmp = 0;b = 0
while num >= 1:
    num = num / 10
    k += 1
    if k > 1:
        tmp = 9 * (10 ** (k - 2))
        b += tmp * (k - 1)
        total9 += tmp

print(b + (n - total9)*k)