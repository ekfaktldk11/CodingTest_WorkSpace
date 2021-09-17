'''
- 별 찍기 - 10
- https://www.acmicpc.net/problem/2447
'''

# 별 찍는 재귀 함수
def draw_star(n):
    global Map

    if n == 3: # n = 3^1 일때 별찍기 모양
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return
    a = n//3
    draw_star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i + k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

#
'''
모든 재귀 마다 3 x 3 매트릭스에 그전에 처리됐던 매트릭스를 규칙에 따라 1 x 1에 넣는 아이디어
'''


N = int(input())

Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map:
    for j in i:
        if j: print('*', end= '')
        else: print(' ', end= '')
    print()

