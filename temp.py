n = int(input())

ary = [0] * (n + 1)

print(ary)

oper = [5, 3, 2]

def f(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    if x == 3:
        return 1
    if x == 4:
        return 2
    if x == 5:
        return 1

    if ary[x] != 0:
        return ary[x]

    for i in range(3):
        if x % oper[i] == 0:
            ary[x] = f(x // oper[i]) + 1
            return ary[x]
    ary[x] = f(x - 1) + 1
    return ary[x]

print(f(n))