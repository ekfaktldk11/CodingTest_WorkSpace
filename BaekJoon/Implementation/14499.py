'''
- 주사위 굴리기
- https://www.acmicpc.net/problem/14499
'''
# 내 풀이 (힌트 얻고 해결 ㅠ)
import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
oper = list(map(int, input().split()))
# 1:동 2:서 3:북 4: 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0, 0]
# 주사위 구현 힌트를 얻음
def dice_chg(dir): # dice[1] 은 항상 윗면을, dice[6] 은 항상 아랫면을
    if dir == 1:
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif dir == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    elif dir == 3:
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    else:
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]

def valid(x, y):
    if x >= 0 and y >= 0 and x < n and y < m: return True
    return False

for op in oper:

    nx, ny = x + dx[op], y + dy[op]
    if not valid(nx, ny): continue
    dice_chg(op)
    x, y = nx, ny
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0
    print(dice[1])
'''
# 결론
- 문제의 핵심 함수인 주사위를 굴렸을때 어느면으로 가는지에 대한 힌트를 얻고 문제를 해결함
- 주사위가 굴릴 때마다 동 - 서 , 남 - 북이 달라지는 경우 때문에 복잡하게 생각했다
- 예를들어 윗면이 1일 때 남 -> 동 -> 동 으로 돌리면 거꾸로된 1이 나타나기 때문에 이런건 어떻게 반영해야할지 어려워했다
- 위처럼 복잡하게 생각할 것 없이 그냥 최초 주사위 모양에서 움직임에 따라 최초 주사위형태가 어떻게 변하고 그것만 반영해주면,
- 몇번을 움직이든 같은 방식으로 반영되기에 이것을 함수로 구현하면 되었다.
'''