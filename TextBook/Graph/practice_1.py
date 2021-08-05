"""
* 팀 결성 문제 (난이도 중상)
- 학교에서 학생들에게 0번부터 N번까지의 번호를 부여
- 처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N + 1개의 팀이 존재
- 이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있음
    (1). '팀 합치기' 연산은 두 팀을 합치는 연산
    (2). '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산
- 선생이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오
- (1 <= N,M <= 100,000) - 제한시간 2초

- 입력 예시
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

- 출력 예시
NO
NO
YES
"""

'''
* 내 풀이 & 해답
'''
def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a > b:
        team[a] = b
    else:
        team[b] = a

def print_same_team(team, a, b):
    if find_team(team, a) != find_team(team, b):
        print("NO")
    else:
        print("YES")


n, m = map(int, input().split())

team = [0] * (n + 1)

for i in range(0, n + 1): #!! key_point -> 문제에서 학생들에게 0번부터 N번까지 번호를 부여했고, 총 N+1개의 팀이 존재한다고 했기에 ~
    team[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0: union_team(team, b, c)
    else: print_same_team(team, b, c)


'''
* 결론
- 그래프 부분을 공부하다 푸는 연습문제 였기에 문제를 읽고 바로 'disjoint_set' 을 이용하여 푸는 문제라고 파악할 수 있었음
- 하지만 그게 아니였다면 어땠을까라고 생각해보니 그리디 방식으로 풀었을 것 같았다. (나는 왜 바로 생각이 안떠오르면 그리디로 접근하는가 ?)
- 주기적으로 봐주어 서로소 집합(disjoint_set)문제가 어떻게 나오는지 유형을 잘 파악하는 것이 좋겠다
'''