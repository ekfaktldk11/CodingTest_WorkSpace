l = 5

ary = [[0 for column in range(l)] for row in range(l)]

for i in range(5):
    a = input().split()
    for j in range(5):
        a[j] = int(a[j])
        ary[i][j] = a[j]

print(ary)

n = int(input())

point = [[0 for column in range(2)] for row in range(n)]

for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    point[_][0] = x
    point[_][1] = y

for p in range(n):
    for i in range(l):
        if (i < point[_][0]):
            y_coord = point[_][1]
            if (ary[i][y_coord] == 0):
                ary[i][y_coord] == 1
            else:
                ary[i][y_coord] == 0
        if (i > point[_][0]):
            y_coord = point[_][1]
            if (ary[i][y_coord] == 0):
                ary[i][y_coord] == 1
            else:
                ary[i][y_coord] == 0
    for j in range(l):
        if (j < point[_][1]):
            x_coord = point[_][0]
            if (ary[x_coord][j] == 0):
                ary[x_coord][j] == 1
            else:
                ary[x_coord][j] == 0
        if (j > point[_][1]):
            x_coord = point[_][0]
            if (ary[x_coord][j] == 0):
                ary[x_coord][j] == 1
            else:
                ary[x_coord][j] == 0

    pass
