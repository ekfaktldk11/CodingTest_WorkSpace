'''
- 덩치
- https://www.acmicpc.net/problem/7568
'''

'''
내 접근 (테스트케이스 o / 정답 x)
# 몸무게로 정렬하고 정렬한 리스트에서 자신의 뒤의 놈보다 키가 크면 같은등수, 작으면 다음 등수

n = int(input())
w_list = []

for num in range(n):
    w, t = map(int, input().split())
    w_list.append((w, t, num))

w_list.sort(reverse=True)

ary = [0] * n

aw = 1
con = 0
ary[w_list[0][2]] = aw
for i in range(1, n):
    idx = w_list[i][2]
    t_n = w_list[i][1]
    t_b = w_list[i - 1][1]
    if t_n < t_b:
        aw = aw + 1 + con
        ary[idx] = aw
        con = 0
    else:
        con += 1
        ary[idx] = aw

for a in ary:
    print(a, end=' ')
'''

# 정답 코드
# item마다 전체를 돌면서 자기보다 덩치가 큰사람이 있으면 등수를 ++ 하면서 출력

n = int(input())
w_list = []

for num in range(n):
    w, t = map(int, input().split())
    w_list.append((w, t))

for item1 in w_list:
    x, y = item1
    aw = 1
    for item2 in w_list:
        nx, ny = item2
        if nx > x and ny > y: aw +=1
    print(aw, end = ' ')



