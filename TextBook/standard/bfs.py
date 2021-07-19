# !!! 여기서 출력하는 순서는 탐색 순서(큐에 들어간 순서)임 !!!
# bfs, dfs 모두 스택이나 큐에 들어가는 순간 visited[i] 해서 방문했다는 처리부터함

# BFS 메소드 정의 -> Queue 사용!
from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue: # 큐가 비었다? popleft()시 queue에 남아있는 것이 없으면 queue의 값이 false 로 변함
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# 1 ~ 8번 노드가 있다고 가정, 각 요소번호에 있는 값들은 해당 노드에 연결된 노드 번호들을 의미
# 1 ~ 8번 노드를 표기해주기 위해 요소번호 0은 빈칸([]) 으로 설정
# 일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 번호가 낮은 순서부터 처리하기 때문에 한 노드에 연결된 노드들의 순서 또한 낮은 순 으로 설정
graph = [
    []
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

# 출력 : 1 2 3 8 7 4 5 6