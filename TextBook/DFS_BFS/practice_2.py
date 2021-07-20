"""
* 미로 탈출 (난이도 '중')
- 한 사람이 N * M 크기의 직사각형 형태의 미로에 갇혀 있음
- 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 함
- 사람의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동가능
- 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있음
- 미로는 반드시 탈출할 수 있는 형태로 제시됨
- 이때 사람이 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오, (시작 및 마지막 칸을 개수에 포함)
- (4 <= N, M <= 200)

- 입력 예시
5 6 (N * M)
101010
111111
000001
111111
111111

- 출력 예시
10
"""

"""
* 내 접근 방법
- DFS/BFS .. 어렵다 .. !
"""

"""
* 해답
"""
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))

"""
* 해답의 접근 방법
- 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하는 BFS 문제임
- 따라서 시작 지점인 (1, 1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 됨
- 시작 지점에서 탈출 지점까지 처음 방문한 값이 '1'인 노드에 방문하기 전의 위치의 값을 더해나가면 시작 지점으로 부터의 해당 노드까지의 최단거리가 입력됨  
"""

"""
* 결론
- 위 소스 코드는 첫 번째 시작위치를 다시 방문할 수 있도록 되어 첫 번째 시작 위치에 해당하는 값이 3으로 변경될 여지가 있음
- 하지만 본 문제에서는 단순히 가장 오른쪽 아래 위치로 이동하는 것을 요구하고 있기 때문에 답 자체에 영향은 없음
- !! 모든 노드(이동 가능한 노드)에 처음 방문할 때 시작 지점으로부터의 거리를 입력해 나가면서 반복문이 끝나면 각 노드엔 시작지점으로 부터의 최단거리가 입력된 다는 것이 포인트 !! 
"""