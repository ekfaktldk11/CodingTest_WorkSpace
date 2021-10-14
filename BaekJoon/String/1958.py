'''
- LCS3
- https://www.acmicpc.net/problem/1958
'''

'''
# 내 풀이 
li = []
for _ in range(3): li.append(input())
li.sort(key=lambda x: len(x))
ans = 0
s = li[0]
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        tmp = s[i:j]
        if li[1].find(tmp) >= 0 and li[2].find(tmp) >= 0: ans = max(ans, len(tmp))

print(ans)
'''

'''
# 내 접근
- 정말 단순히, 길이 오름차순으로 정렬하고 제일 길이가 작은 문자열에서 만들수 있는 모든 연속 문자열 들마다 남은 두 문자열에 있는지 확인하고 최대값을 업데이트 했다

'''

import sys
input = sys.stdin.readline

f = input().strip()
s = input().strip()
t = input().strip()

fl = len(f)
sl = len(s)
tl = len(t)

dp = [[[-1] * tl for i in range(sl)] for j in range(fl)] # 3차원 행렬

def LCS(a, b, c): # LCS 보통 2개의 문자열이 인풋, 3개일 때 ..?
    if a < 0 or b < 0 or c < 0:
        return 0

    if dp[a][b][c] == -1:
        dp[a][b][c] = 0

        if f[a] == s[b] == t[c]:
            dp[a][b][c] = LCS(a - 1, b - 1, c - 1) + 1
        else:
            dp[a][b][c] = max(max(LCS(a, b - 1, c), LCS(a - 1, b, c)), LCS(a, b, c - 1))

    return dp[a][b][c]

print(LCS(fl - 1, sl - 1, tl - 1))

'''
- 내 방법이 왜 안되는지 ..흠 아직도 잘 이해가 안가네..
- 처음 두 줄의 LCS를 찾고 그 결고와 마지막 줄의 LCS 를 찾는 순차적인 방법도 있음
'''