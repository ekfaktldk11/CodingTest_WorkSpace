'''
- 치즈
- https://www.acmicpc.net/problem/2636
'''

'''
내 접근
# 치즈가 있는 칸들의 좌표 목록을 큐에 넣고 녹지 않는 조건이면 다시 큐에 넣어서 풀이
# BFS를 사용하여 모든 치즈로 부터 가장자리에 닿는 방법이 있으면 해당 치즈는 다음 시행에서 녹는다는 것을 판별
# 하지만 치즈에 둘러쌓여 있는 구멍인 경우, 계속 그 구멍을 반복해서 순회하는 오류 발생

from collections import deque

m, n = map(int, input().split())
ary = []
for _ in range(m): ary.append(list(map(int, input().split())))

q = deque([])
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if ary[i][j] == 1: q.append((i, j))


def melt(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q_ = deque([(x, y)])
    while q_:
        a, b = q_.popleft()
        print(a, b)
        for d in range(4):
            nx, ny = a + dx[d], b + dy[d]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and ary[nx][ny] == 0:
                if nx == 0 or ny == 0: return True
                q_.append((nx, ny))
    return False


round = 0
while q:
    total = len(q)
    print(q)
    round += 1
    tmp = []
    for _ in range(total):
        x, y = q.popleft()
        if not melt(x, y): q.append((x, y))
        else: tmp.append((x, y))
    for x, y in tmp:
        ary[x][y] = 0
print(round)
print(total)
'''

# 정답 코드
# 구멍인 (0, 0)부터 시작해서 BFS 로 순회하여 치즈를 만나면 치즈를 0으로 바꾸고 방문처리

from collections import deque
m, n = map(int, input().split())
ary = []
for _ in range(m): ary.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

num_of_c = []
def cheese():
    visited = [[False] * n for _ in range(m)]
    q = deque([(0, 0)])
    visited[0][0] = True
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n and not visited[nx][ny]:
                if ary[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    ary[nx][ny] = 0
                    count += 1
                    visited[nx][ny] = True
    num_of_c.append(count)
    return count
r = 0
while 1:
    count = cheese()
    if count == 0: break
    r += 1
print(r)
print(num_of_c[-2])

'''
결론
# 나는 치즈로부터 녹는 치즈를 찾았지만 해답은 구멍으로부터 녹는 치즈를 찾는 것이었다.
# 녹는 치즈를 어디서 부터 찾을 것인지에 대한 접근을 다양하게 하면 풀이법을 찾을 수 있다!
# 들른 지점을 다시 들르지 않기 위해 방문처리는 필수!
'''


