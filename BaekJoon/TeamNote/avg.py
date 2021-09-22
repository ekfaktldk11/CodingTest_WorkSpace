'''
# 산술 평균
- 산술 평균이 정수일 경우
- 산술 평균을 구할 때 단순히 sum(n_list) // n 으로하면 정답이 아닐 경우가 대부분 (나눈몫 != 산술평균)
- round()함수를 사용하여 산술평균을 구함
'''
n_list = list(map(int, input().split()))

avg = round(sum(n_list) / len(n_list))