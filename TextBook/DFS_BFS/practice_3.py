
# 341pg 연구소 (확산문제)

from itertools import combinations
import copy

# n, m
n, m = map(int, input().split())

graph = []

virus = []
wall = []

# 그래프 채우기
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

# 바이러스 위치, 벽이 들어갈수 있는 위치 들을 각 해당하는 리스트에 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            wall.append((i, j))
        else: continue

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y, lab):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if lab[nx][ny] == 0:
                lab[nx][ny] = 2
                virus(nx, ny, lab)

# 벽을 설치 후 바이러스가 확산 되었을 경우 안전한 장소의 수를 세는 함수 생성
def safe_zone(wall_list):
    count = 0
    # 2차원 배열 복사
    lab = copy.deepcopy(graph)


    # 3개의 벽 세우기
    for row, col in wall_list:
        lab[row][col] = 1

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2: virus(i, j, lab)


    # 안전한 장소 숫자 count
    for i in range(n):
        # print(lab[i])
        for j in range(m):
            if lab[i][j] == 0: count += 1

    return count

# 모든 '0' 을 가지는 값 중에서 3개의 벽을 세우는 뽑는 조합 계산
candidates = list(combinations(wall, 3))

max_safe = 0
for candidate in candidates:
    max_safe = max(max_safe, safe_zone(candidate))

print(max_safe)