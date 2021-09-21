'''
- 통계학
- https://www.acmicpc.net/problem/2108
'''

from collections import Counter

n = int(input())
li = []
for _ in range(n):
    i = int(input())
    li.append(i)

avg = round(sum(li) / n) # <-- 산술평균(N개의 수들의 합을 N으로 나눈값) --- 난 sum(li) // n 으로 해서 자꾸 틀렸었음.
mid = sorted(li)[n // 2]

li.sort()
cnt = Counter(li).most_common(2) # <-- 최빈값 두개에 대한 정보 // 리스트 정렬후에 most_common을 사용해야 정렬된 값을 기반으로 값을 탐색

if len(cnt) == 1: mo = cnt[0][0]
else:
    if cnt[0][1] == cnt[1][1]: mo = cnt[1][0]
    else: mo = cnt[0][0]

rng = max(li) - min(li)

print(avg, mid, mo, rng, sep='\n')