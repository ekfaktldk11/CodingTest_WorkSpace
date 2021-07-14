# 3항 연산 x if(cond(x,y)) else y
a, b = input().split()
a = int(a)
b = int(b)
print(a if(a >= b) else b)