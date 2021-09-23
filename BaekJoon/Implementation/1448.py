'''
- 방번호
- https://www.acmicpc.net/problem/1448
'''

import re
n = input()
n_ary = [0] * 9
for num in n:
    num = int(num)
    if num == 9: n_ary[6] += 1
    else: n_ary[num] += 1
else:
    if n_ary[6] % 2: n_ary[6] = n_ary[6]//2 + 1
    else: n_ary[6] = n_ary[6]//2

print(max(n_ary))