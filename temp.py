def recur(n):
    #global ary
    s_n = str(n)
    for a in s_n:
        n += int(a)
    if n >= 10000: return
    ary[n] = n
    recur(n)

ary = [0] * 10000

for i in range(1, 10000):
    if ary[i]: continue
    else: recur(i)

for i in range(1, len(ary)):
    if not ary[i]: print(i)