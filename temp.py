# n, m = map(int, input().split())
# s = list(map(int, input().split()))
#
# ary = [0] * (m + 1)
#
# for i in range(1, m + 1):
#     for j in range(n):
#         if s[j] == i:
#             ary[i] += 1
#
# def count(num):
#     val = 0
#     for i in range(1, num):
#         val += i
#     return val
#
# total_count = count(n)
#
# sum = 0
#
# for i in range(1, m + 1):
#     sum += count(ary[i])
#
# print(total_count - sum)
import heapq

food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):
    answer = 0
    left = len(food_times)
    for i in range(left):
        heapq.heappush(food_times[i], i)
    while True:
        item = heapq.heappop()
        if (item[0] * left) < k:
            k -= item[0] * left
            left -= 1
            continue
        else:
            answer = (k + 1) % len(food_times)
            break

    return answer

print(solution(food_times, k))