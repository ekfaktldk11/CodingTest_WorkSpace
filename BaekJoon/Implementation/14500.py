'''
- 테트로미노
- https://www.acmicpc.net/problem/14500
'''

'''
# 내 접근 (failed.py) -> 테케는 다 통과 but, 효율성에서 탈락(시간초과)
import copy
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

total = []

def valid(x, y):
    if x >= 0 and y >= 0 and x < n and y < m: return True
    return False

def dfs(li, x, y, s, count):
    if len(li) > 3:
        total.append(s)
        return

    if len(li) == 3:
        x1, y1 = li[0]
        x2, y2 = li[1]
        x3, y3 = li[2]

        if x1 == x2 == x3:
            if (y1 + y3) / 2 == y2:
                nx, ny = x2 + dx[0], y2 + dy[0] # 북
                if valid(nx, ny):
                    total.append(s + graph[nx][ny])
                nx, ny = x2 + dx[2], y2 + dy[2] # 남
                if valid(nx, ny):
                    total.append(s + graph[nx][ny])

        if y1 == y2 == y3:
            if (x1 + x3) / 2 == x2:
                nx, ny = x2 + dx[1], y2 + dy[1]  # 동
                if valid(nx, ny):
                    total.append(s + graph[nx][ny])
                nx, ny = x2 + dx[3], y2 + dy[3]  # 남
                if valid(nx, ny):
                    total.append(s + graph[nx][ny])


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if valid(nx, ny) and (nx, ny) not in li:
            t = s
            li_c = copy.deepcopy(li) # 여기서 메모리, 시간 초과 유발하는듯
            li_c.append((nx, ny))
            t += graph[nx][ny]
            count += 1
            dfs(li_c, nx, ny, t, count)


for x in range(n):
    for y in range(m):
        li = []
        li.append((x, y))
        dfs(li, x, y, graph[x][y], 1)

print(max(total))
'''

# 해답 https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-14500-%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8 을 참고했음
import sys; input = sys.stdin.readline

def dfs(r, c, idx, total): # dfs 사용법은 비슷함
    global ans
    if idx == 3:
        if total > ans:
            ans = total
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1: # 'ㅗ' 모양 만들기, idx 가 1일 때 즉, 2개의 블록을 형성 했을 때, 새로운 블록이 아닌 기존 블록에서 dfs 탐색을 행해주며 ㅗ 모양 생성가능
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)

'''
# 결론
1. deepcopy.copy() 로 인해 메모리 초과가 될 수 있다는 것을 알아두길
2. 'ㅗ' 모양 만들기, idx 가 1일 때 즉, 2개의 블록을 형성 했을 때, 새로운 블록이 아닌 기존 블록에서 dfs 탐색을 행해주며 ㅗ 모양 생성가능
'''