 # 565 pg 확인
t = int(input())

# 오른쪽 위, 오른쪽, 오른쪽 아래
dx = [-1, 0, 1]


def backward_value(updated_graph, x, y, n, m):
    if x >= 1 and x < (n + 1) and y >= 1 and y < (m + 1):
        return updated_graph[x][y]
    else:
        return 0

def solution():
    n, m = map(int, input().split())

    ary = [[0] * (m + 1) for _ in range(n + 1)]

    d = [[0] * (m + 1) for _ in range(n + 1)]

    temp = list(map(int, input().split()))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ary[i][j] = temp.pop(0)


    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for k in range(3):
               d[i][j] = max(d[i][j], ary[i][j] + backward_value(d, i + dx[k], j - 1, n, m))

    max_val = 0
    # for i in range(1, n + 1):
    #     for j in range(1, m + 1):
    #         max_val = max(max_val, d[i][j])
    for i in range(n):
        max_val = max(max_val, d[i][m]) # 짜피 각 라인에서 맨 끝의 값들이 제일 큰 값을 가질수밖에 없음

    print(d)
    print(max_val)

for g in range(t):
    solution()