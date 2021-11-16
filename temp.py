n, k = map(int, input().split())
velt = [0] * (n * 2)
ind = list(map(int, input().split()))
c = 0


def velt_move():
    tmp = velt.pop()
    velt.insert(0, tmp)
    tmp = ind.pop()
    ind.insert(0, tmp)


def robot_move():
    tmp = []
    for i in range(2 * n - 1):
        if velt[i] == 1 and velt[i + 1] == 0 and ind[i + 1] >= 1:
            tmp.append(i)
    for i in tmp:
        velt[i], velt[i + 1] = velt[i + 1], velt[i]
        ind[i + 1] -= 1



def robot_on():
    if ind[0] >= 1: velt[0] = 1


def check_ind():
    if ind.count(0) >= k: return False
    return True


while check_ind():
    c += 1
    velt_move()
    robot_move()
    robot_on()
print(c)