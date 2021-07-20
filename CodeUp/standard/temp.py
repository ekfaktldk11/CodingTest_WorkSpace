# n, m = map(int, input().split())
#
# ary = []
#
# for i in range(n):
#     ary.append(list(map(int, input().split())))
#
# print(ary)
# def dfs(x, y):
#     if x < 0 or x > n or y < 0 or y > m: #범위 초과
#         return False
#     if ary[x][y] == 0: # 처음 채우는 음료수 군집
#         ary[x][y] == 1
#         dfs(x - 1, y) #상
#         dfs(x + 1, y) #하
#         dfs(x, y - 1) #좌
#         dfs(x, y + 1) #우
#         return True
#     return False
#
# count = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True: # 새로운 군집 형성시 count ++
#             count += 1
#
# print(count)

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    # 여기서 중요한 것이 graph.append(list(map(int, input().split())))로 실행 시 [[000111011], [110110010], ...] 이런식으로 할당됨
    # 공백없이 입력될 때는 graph.append(list(map(int, input())))로 실행 해야 [[0, 1, 0 ...]] 이런식으로 할당됨
    graph.append(list(map(int, input())))

print(graph)

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    #global graph
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면 (음료수를 채우지 않았다면)
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리 (빈칸에 음료수 채우기)
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력