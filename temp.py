# import sys
# # 채택된 식량 창고 check
# d = [0] * 100
#
# # 식량 창고 수
# n = int(input())
#
# # 창고 마다의 식량 수
# n_ary = list(map(int, sys.stdin.readline().split()))
# n_ary.append(0)
# n_ary.append(0)
# n_ary.append(0)
# n_ary.append(0)
# n_ary.append(0)
# n_ary.append(0)
#
#
# print(n_ary)
#
# for i in range(0, n + 2, 2):
#     r1 = n_ary[i] + max(n_ary[i + 2], n_ary[i + 3])
#     r2 = n_ary[i + 1] + max(n_ary[i + 3], n_ary[i + 4])
#     if (r1 >= r2): d[i] = 1
#     else: d[i + 1] = 1
#
# sum = 0
# for i in range(n):
#     if d[i] == 1: sum += n_ary[i]
# print(d)
# print(sum)

# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(Bottom Up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n): # 3 <= N 이니까
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])
