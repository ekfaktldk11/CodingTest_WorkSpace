'''
- 로봇 청소기
- https://www.acmicpc.net/problem/14503
'''

'''
# 내 접근 (failed.py)
n, m = map(int, input().split())
r, c, dir = map(int, input().split())

graph = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 이 valid 라는 걸 너무쓰다 버릇하니 완전탐색에서 valid 부터 구현하고 시작하니 문제가 산으로 가지...
def valid(x, y): 
    if x >= 0 and y >= 0 and x < n and y < m and graph[x][y] == 0:
        return True
    return False

def back(x, y, d):
    nd = d - 2
    if nd == -1: nd == 3
    if nd == -2: nd == 2
    return x + dx[nd], y + dy[nd]


def next_dir(d):
    d -= 1
    if d == -1: d = 1
    return d

answer = 0
x, y, d = r, c, dir

while True:
    flag = False
    if valid(x, y): # 그냥 graph 값이 0 즉, 청소할 수 있는 지만 판단하면 되는 것을 ...
        answer += 1
        graph[x][y] = 1 # 그리고 여기서도 청소 완료된것을 '벽' 이라는 값과 같은 값을 쓰면 문제에 혼동이 오지요...
    for _ in range(4):
        d = next_dir(d)
        nx, ny = x + dx[d], y + dy[d]
        if valid(nx, ny):
            x, y = nx, ny
            flag = True
            break
    if flag: continue
    else:
        nx, ny = back(x, y, d)
        if valid(nx, ny): continue # 벽만아니면 continue!!!
        break
print(answer)
'''

# 수정후 (solved.py)
n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def back(x, y, d):
    nd = d - 2
    if nd == -1: nd == 3
    if nd == -2: nd == 2
    return x + dx[nd], y + dy[nd]

def next_dir(d):
    d -= 1
    if d == -1: d = 3
    return d

answer = 0

while True:
    flag = False
    if graph[x][y] == 0:
        answer += 1
        graph[x][y] = 2
    for _ in range(4):
        d = next_dir(d)
        nx, ny = x + dx[d], y + dy[d]
        if graph[nx][ny] == 0:
            x, y = nx, ny
            flag = True
            break
    if flag: continue
    else:
        nx, ny = back(x, y, d)
        if graph[nx][ny] != 1:
            x, y = nx, ny
            continue
        break
print(answer)


'''
# 결론
1. 문제를 똑바로 읽을 것
2. 문제가 요구하는 것만을 구사할 것
3. 문제 좀 풀어봤다고 쉬운문제라고 '~이거 겠지' 라는 생각으로 자주쓰이는 함수 구현하다가 큰 코 다침
'''

